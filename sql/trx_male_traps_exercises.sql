INSERT INTO exercise (name, description, category) VALUES ('TRX Y Raise', 'Hold the TRX straps and lean away from the anchor point until the straps are taut.
Keep both elbows mostly extended and raise both arms out and upwards.
You should make a Y shape with your arms during the back portion of the exercise.', 'traps') ON CONFLICT (name) DO NOTHING;
