CREATE TABLE food (
    food_id INT PRIMARY KEY,
    name TEXT
);

INSERT INTO food VALUES
    (1, 'banana'),
    (2, 'cellery'),
    (3, 'carrot'),
    (4, 'pretzel'),
    (5, 'oatmeal'),
    (6, 'water'),
    (7, 'vitamin pills');

CREATE TABLE flavor (
    flavor_id INT PRIMARY KEY,
    food_id INT,
    name TEXT
);

INSERT INTO flavor VALUES
    (1, 1, 'sweet'),
    (2, 1, 'soft'),
    (3, 2, 'crunchy'),
    (4, 3, 'sweet'),
    (5, 3, 'crunchy'),
    (6, 4, 'salty'),
    (7, 4, 'crunchy'),
    (8, 4, 'bready'),
    (9, 5, 'bland'),
    (10, 5, 'soft');

