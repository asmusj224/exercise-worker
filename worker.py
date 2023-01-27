import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime, timezone
import psycopg2
import logging
import logging.handlers
from dotenv import load_dotenv
import pytz


load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

BASE_QUERY = '''
   select ranked_exercises.name, ranked_exercises.description, ranked_exercises.category from 
   (SELECT exercise.*,
    rank() OVER (PARTITION BY category ORDER BY random())
    FROM exercise) ranked_exercises
'''
CORE_WHERE_CLAUSE = "(rank = 1 and category = 'Core')"

lower_body = f"{BASE_QUERY} where rank <= 6 and category = 'Legs' or {CORE_WHERE_CLAUSE}"
upper_body = f"{BASE_QUERY} where rank <= 2 and category IN ('Chest', 'Back', 'Bicep', 'Traps', 'Shoulders', 'Triceps') or {CORE_WHERE_CLAUSE}"
yoga = f"{BASE_QUERY} where rank = 1 and category = 'yoga'"

workout_splits = [lower_body, upper_body, yoga, lower_body, upper_body]

PST = pytz.timezone('US/Pacific')
utc_dt = datetime.now(timezone.utc)


def generate_workout():
    try:
        today_dt = utc_dt.astimezone(PST).today()
        logger.info(f'Today {datetime.now(timezone.utc)}')
        to_email = os.environ.get('TO_EMAIL')
        from_email = os.environ.get('FROM_EMAIL')
        conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        day_of_week_index = today_dt.weekday()
        cursor = conn.cursor()
        cursor.execute(workout_splits[day_of_week_index])
        rows = cursor.fetchall()
        message = ''
        subject = f"Workouts {today_dt.strftime('%Y-%m-%d')}"
        for row in rows:
            exercise_name, exercise_description, exercise_category = row
            message += f'<h3>{exercise_name}</h3> <b>{exercise_category}</b> <p>{exercise_description}</p>'
        email = Mail(from_email=from_email, to_emails=to_email, subject=subject, html_content=message)
        sg.send(email)


    except Exception as e:
        logger.info(f'An error occured {e}')

if __name__ == "__main__":
    generate_workout()


