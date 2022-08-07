CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)

);

SELECT * FROM users;

CREATE TABLE team(
    team_id SERIAL PRIMARY KEY,
    user_id SERIAL,
    win_id INTEGER
);

SELECT * FROM team;

CREATE TABLE wins(
    win_id SERIAL PRIMARY KEY,
    team_id VARCHAR(30),
    user_id SERIAL
);

SELECT * FROM wins;
