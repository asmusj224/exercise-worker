from apscheduler.schedulers.blocking import BlockingScheduler
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime
import psycopg2
from dotenv import load_dotenv



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

load_dotenv()

schedule = BlockingScheduler()

@schedule.scheduled_job('cron', day_of_week='mon-fri', hour=5)
def generate_workout():
    try:
        conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        day_of_week_index = datetime.today().weekday()
        cursor = conn.cursor()
        cursor.execute(workout_splits[day_of_week_index])
        rows = cursor.fetchall()
        message = ''
        subject = 'Workouts'
        for row in rows:
            exercise_name, exercise_description, exercise_category = row
            message += f'<h3>{exercise_name}</h3> <b>{exercise_category}</b> <p>{exercise_description}</p>'
        email = Mail(from_email="me@jeffasmus.com", to_emails="jeffrey.asmus88@gmail.com", subject=subject, html_content=message)
        sg.send(email)


    except Exception as e:
        print('Worker failed')
        print(e)


schedule.start()
