INSERT INTO exercise (name, description, category) VALUES ('Band Crunch', 'Place the band at the highest anchor point you have available. Grab both ends of the band and fall into a kneeling position.
Push your hips back flexing at the spine.
Squeeze your abs and then extend at the hips and spine back to the starting position.', 'abdominals') ON CONFLICT (name) DO NOTHING;
