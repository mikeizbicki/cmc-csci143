/*
 * For each insert statement below, calculate the number of bytes used by the row
 */

--------------------------------------------------------------------------------

CREATE TABLE example1 (
    a INTEGER
);

INSERT INTO example1 (1);

-- header:
-- data:
-- padding:
-- total:

INSERT INTO example1 (NULL);

-- header:
-- data:
-- padding:
-- total:

--------------------------------------------------------------------------------

CREATE TABLE example2 (
    a SMALLINT,
    b BIGINT,
    c INTEGER
);

INSERT INTO example2 (1,2,3);

-- header:
-- data:
-- padding:
-- total:

INSERT INTO example2 (1,NULL,3);

-- header:
-- data:
-- padding:
-- total:

INSERT INTO example2 (NULL,NULL,NULL);

-- header:
-- data:
-- padding:
-- total:

CREATE TABLE example3 (
    b BIGINT,
    c INTEGER,
    a SMALLINT
);

INSERT INTO example3 (2,3,1);

-- header:
-- data:
-- padding:
-- total:

INSERT INTO example3 (NULL,3,1);

-- header:
-- data:
-- padding:
-- total:

INSERT INTO example3 (NULL,NULL,NULL);

-- header:
-- data:
-- padding:
-- total:

--------------------------------------------------------------------------------

CREATE TABLE example3 (
    c1 SMALLINT,
    c2 SMALLINT,
    c3 SMALLINT,
    c4 SMALLINT,
    c5 SMALLINT,
    c6 SMALLINT,
    c7 SMALLINT,
    c8 SMALLINT,
    c9 SMALLINT
);

INSERT INTO example3 (1,2,3,4,5,6,7,8,9);

-- header:
-- data:
-- padding:
-- total:

INSERT INTO example3 (1,2,NULL,4,5,6,7,8,9);

-- header:
-- data:
-- padding:
-- total:

INSERT INTO example3 (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

-- header:
-- data:
-- padding:
-- total:
