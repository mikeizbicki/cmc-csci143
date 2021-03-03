CREATE TABLE myfilm (
    film_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    special_features TEXT[]
);

INSERT INTO myfilm (title,special_features) VALUES
    ('harry potter and the philosopher''s stone', ARRAY['Trailer']),
    ('harry potter and the chamber of secrets', ARRAY['Trailer','Director''s Commentary']),
    ('harry potter and the prisoner of azkaban', ARRAY[]::TEXT[]),
    ('harry potter and the goblet of fire', null),
    ('harry potter and the order of the phoenix', ARRAY['Trailer','Director''s Commentary']),
    ('harry potter and the half-blood prince', ARRAY['Director''s Commentary']),
    ('harry potter and the deathly hollows - part 1', ARRAY['Trailer','Director''s Commentary', 'Behind the Scenes']),
    ('harry potter and the deathly hollows - part 2', ARRAY['Director''s Commentary', 'Behind the Scenes']);

