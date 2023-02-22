
-- ARRAY --

CREATE TABLE food_array (
    id INT PRIMARY KEY,
    food TEXT,
    flavors TEXT[]
);

INSERT INTO food_array VALUES
    (1, 'banana', ARRAY['sweet','soft']),
    (2, 'cellery', ARRAY['crunchy']),
    (3, 'carrot', ARRAY['sweet','crunchy']),
    (4, 'pretzel', ARRAY['salty','crunchy','bready']),
    (5, 'oatmeal', '{"bland","soft"}'),
    (6, 'water', ARRAY[]::TEXT[]),
    (7, 'vitamin pills', '{}');

-- NORMALIZED --

CREATE TABLE food_normalized (
    food_normalized_id INT PRIMARY KEY,
    food TEXT
);

INSERT INTO food_normalized VALUES
    (1, 'banana'),
    (2, 'cellery'),
    (3, 'carrot'),
    (4, 'pretzel'),
    (5, 'oatmeal'),
    (6, 'water'),
    (7, 'vitamin pills');

CREATE TABLE flavor (
    food_normalized_id INT,
    flavor TEXT
);

INSERT INTO flavor VALUES
    (1, 'sweet'),
    (1, 'soft'),
    (2, 'crunchy'),
    (3, 'sweet'),
    (3, 'crunchy'),
    (4, 'salty'),
    (4, 'crunchy'),
    (4, 'bready'),
    (5, 'bland'),
    (5, 'soft');

