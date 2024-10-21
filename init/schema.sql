CREATE TABLE IF NOT EXISTS 'pets' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS 'people' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    pet_id INTEGER,
    FOREIGN KEY (pet_id) REFERENCES pets (id)
);

INSERT INTO
    pets (name, type)
VALUES ('Fluffy', 'cat'),
    ('Spot', 'dog'),
    ('Goldie', 'fish'),
    ('Buddy', 'dog'),
    ('Cobra', 'snake'),
    ('Mickey', 'mouse'),
    ('Perry', 'platypus'),
    ('Spike', 'porcupine'),
    ('Snoopy', 'beagle'),
    ('Tweety', 'canary'),
    ('Wilbur', 'pig'),
    ('Yogi', 'bear');