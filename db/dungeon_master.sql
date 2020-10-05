DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS parties;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE parties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    next_game VARCHAR(255)
);

CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    race VARCHAR(255),
    archetype VARCHAR(255),
    level INT,
    armour INT,
    magic BOOLEAN, 
    weight INT,
    perception INT,
    insight INT,
    immunity VARCHAR(255),
    vision VARCHAR(255),
    language VARCHAR(255),
    aura VARCHAR(255),
    enmity VARCHAR(255), 
    exhaustion INT,
    player_id SERIAL REFERENCES players(id) ON DELETE CASCADE,
    party_id SERIAL REFERENCES parties(id) ON DELETE CASCADE
);
