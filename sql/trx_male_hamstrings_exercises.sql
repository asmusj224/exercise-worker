INSERT INTO exercise (name, description, category) VALUES ('TRX Hamstring Curl', 'Start by facing the TRX straps and positioning yourself in a push-up position with your hands on the ground and your feet in the TRX foot cradles.
Keeping your core engaged and body in a straight line, bend your knees and bring your heels towards your glutes.
Pause for a moment at the top of the movement, then slowly lower your legs back to the starting position.', 'hamstrings') ON CONFLICT (name) DO NOTHING;
