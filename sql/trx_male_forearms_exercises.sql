INSERT INTO exercise (name, description, category) VALUES ('TRX Reverse Curl', 'Stand facing the TRX straps and grasp the handles with both hands, palms facing away from your body.
Walk back until the straps are taut, keeping your arms straight.
Slowly curl your hands towards your shoulders, keeping your elbows close to your body.', 'forearms') ON CONFLICT (name) DO NOTHING;
