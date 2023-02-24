INSERT INTO exercise (name, description, category) VALUES ('TRX Calf Raise', 'Hold the TRX straps under your arms and the handles in your armpits.
Lean forward against the straps.
Keep your body straight and initiate the calf raise by raising your heels off the ground.', 'calves') ON CONFLICT (name) DO NOTHING;
