INSERT INTO exercise (name, description, category) VALUES ('Band Calf Raise', 'Attach band to a low anchor point.
Take a few steps away until the band is taut.
Lean back slightly. Raise your heels straight up and down', 'calves') ON CONFLICT (name) DO NOTHING;
