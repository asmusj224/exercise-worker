INSERT INTO exercise (name, description, category) VALUES ('TRX Skullcrusher', 'Hold the two TRX straps and lean forward. The straps should be over each shoulder.
Keep your elbows tucked in and then flex and extend at the elbows.', 'triceps') ON CONFLICT (name) DO NOTHING;
INSERT INTO exercise (name, description, category) VALUES ('TRX Pushup', 'Hold the two TRX straps and lean forward. The straps should be over each shoulder.
Keep your elbows tucked in and then flex and extend at the elbows.', 'triceps') ON CONFLICT (name) DO NOTHING;
