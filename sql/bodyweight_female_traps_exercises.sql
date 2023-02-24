INSERT INTO exercise (name, description, category) VALUES ('Elevated Pike Press', 'Use a bench or an object to elevate your feet.
Lower your head towards the floor by bending your elbows
Push through your hands and return to the starting pike position.
Repeat', 'traps') ON CONFLICT (name) DO NOTHING;
INSERT INTO exercise (name, description, category) VALUES ('Elevated Pike Shoulder Shrug', 'Use a bench or an object to elevate your feet.
Lower your head towards the floor by bending your elbows
Push through your hands and return to the starting pike position.
Repeat', 'traps') ON CONFLICT (name) DO NOTHING;
