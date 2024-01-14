-- custom enum types

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'sport_type') THEN
        CREATE TYPE sport_type AS ENUM (
        'Soccer',
        'Basketball',
        'Football',
        'Baseball',
        'Cricket',
        'Rugby',
        'Hockey',
        'Volleyball',
        'Handball',
        'Softball'
    );  
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'league_type') THEN
        CREATE TYPE league_type AS ENUM (
            'league',
            'cup',
            'super-cup'
        );
    END IF;
END$$;

-- uuid generator
-- add uuid generator

-- geographical data 

CREATE TABLE IF NOT EXISTS countries (
    uuid UUID PRIMARY KEY NOT NULL DEFAULT generate_uuid_v4(),
    "code" CHAR(2) NOT NULL,
    name VARCHAR(55) NOT NULL,
	PRIMARY KEY (uuid)
);


CREATE TABLE IF NOT EXISTS venues (
    uuid UUID PRIMARY KEY NOT NULL DEFAULT generate_uuid_v4(),
    id INT NOT NULL,
    name VARCHAR(55),
    city_name VARCHAR(55)
);

CREATE TABLE IF NOT EXISTS teams (
    uuid UUID PRIMARY KEY NOT NULL DEFAULT generate_uuid_v4(),
    id INT NOT NULL,
    name VARCHAR(55) NOT NULL,
    code CHAR(3) NOT NULL,
    sport sport_type NOT NULL,
    home_venue_id INT,

    FOREIGN KEY (home_venue_id) REFERENCES venues (uuid)
);


CREATE TABLE IF NOT EXISTS leagues (
    uuid UUID PRIMARY KEY NOT NULL DEFAULT generate_uuid_v4(),
    id INT NOT NULL,
    name VARCHAR(55) NOT NULL,
    sport sport_type NOT NULL,
    country_id CHAR(2) NOT NULL,
    type league_type NOT NULL,

    FOREIGN KEY (country_id) REFERENCES countries (uuid)
);

CREATE TABLE IF NOT EXISTS seasons (
    uuid UUID PRIMARY KEY NOT NULL DEFAULT generate_uuid_v4(),
    id INT NOT NULL,
    league_id INT NOT NULL,
    sport sport_type NOT NULL,
    year INT NOT NULL,
    "start" DATE NOT NULL,
    "end" DATE NOT NULL,

    FOREIGN KEY (league_id) REFERENCES leagues (uuid)
);

CREATE TABLE IF NOT EXISTS fixtures (
    uuid UUID PRIMARY KEY NOT NULL DEFAULT generate_uuid_v4(),
    id INT NOT NULL,
    sport sport_type NOT NULL,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    venue_id INT NOT NULL,
    "timestamp" TIMESTAMP,
    is_finished BOOLEAN NOT NULL DEFAULT FALSE,
    is_home_team_home BOOLEAN NOT NULL DEFAULT TRUE
);

