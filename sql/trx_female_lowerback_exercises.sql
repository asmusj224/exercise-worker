INSERT INTO exercise (name, description, category) VALUES ('TRX Ab Rollout', 'Grasp the TRX handles with both hands, keeping your arms extended and your shoulders away from your ears.
Keep your abs engaged, roll forward onto your toes, and extend your arms in front of you.
Slowly lower your body down to the ground, keeping your arms straight and your abs engaged.
When your head gets between your arms, pause for a moment and then use your abs to pull your body back up to the starting position.', 'lowerback') ON CONFLICT (name) DO NOTHING;
