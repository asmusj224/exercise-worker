INSERT INTO exercise (name, description, category) VALUES ('Chin Ups', 'Grab the bar shoulder width apart with a supinated grip (palms facing you)
With your body hanging and arms fully extended, pull yourself up until your chin is past the bar.
Slowly return to starting position. Repeat.', 'biceps') ON CONFLICT (name) DO NOTHING;
