CREATE TABLE food (
    id INT PRIMARY KEY,
    name TEXT,
    flavors TEXT[]
);

INSERT INTO food VALUES
    (1, 'banana', ARRAY['sweet','soft']),
    (2, 'cellery', ARRAY['crunchy']),
    (3, 'carrot', ARRAY['sweet','crunchy']),
    (4, 'pretzel', ARRAY['salty','crunchy','bready']),
    (5, 'oatmeal', '{"bland","soft"}'),
    (6, 'water', ARRAY[]::TEXT[]),
    (7, 'vitamin pills', '{}');
