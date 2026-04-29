-- 1. go to pgAdmin
-- 2. open localhost:5433/browser/
-- 3. browser go to folder
-- 4. insert all create tables to store 

CREATE EXTENSION IF NOT EXISTS citext;
-- Full schema for travel blog will be in week3 as it was the simplest form 
CREATE TABLE users( --create users 
 id BIGSERIAL PRIMARY KEY,
 username CITEXT UNIQUE NOT NULL,
 email CITEXT UNIQUE NOT NULL,
 password_hash TEXT NOT NULL,
 created_at TIMESTAMPTZ DEFAULT now()
);
CREATE TABLE profiles( --create profiles 
 id BIGSERIAL PRIMARY KEY,
 user_id BIGINT UNIQUE REFERENCES users(id) ON DELETE CASCADE,
 display_name TEXT,
 bio TEXT,
 home_city TEXT,
 home_country TEXT,
 avatar_url TEXT
);
CREATE TABLE destinations( --create destinations for places traveling to 
 id BIGSERIAL PRIMARY KEY,
 city TEXT NOT NULL,
 country TEXT NOT NULL,
 region TEXT,
 iso_code TEXT
);
CREATE TABLE posts( --create posts of each location  
 id BIGSERIAL PRIMARY KEY,
 user_id BIGINT REFERENCES users(id),
 title TEXT NOT NULL,
 body TEXT NOT NULL,
 rating INT CHECK (rating BETWEEN 1 AND 5),
 is_published BOOLEAN DEFAULT false,
 published_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ DEFAULT now()
);
CREATE TABLE trips( --create trips, can be for all places traveling to 
 id BIGSERIAL PRIMARY KEY,
 user_id BIGINT REFERENCES users(id),
 destination_id BIGINT REFERENCES destinations(id),
 total_cost NUMERIC(10,2),
 trip_days INT,
 safety_score INT,
 trip_notes TEXT,
 started_at TIMESTAMPTZ,
 ended_at TIMESTAMPTZ
);
CREATE TABLE tags( --create tags of what you want  
 id BIGSERIAL PRIMARY KEY,
 name CITEXT UNIQUE
);
CREATE TABLE post_tags(
 post_id BIGINT REFERENCES posts(id) ON DELETE CASCADE,
 tag_id BIGINT REFERENCES tags(id) ON DELETE CASCADE,
 PRIMARY KEY(post_id, tag_id)
);
CREATE TABLE post_destinations(
 post_id BIGINT REFERENCES posts(id) ON DELETE CASCADE,
 destination_id BIGINT REFERENCES destinations(id) ON DELETE CASCADE,
 PRIMARY KEY(post_id, destination_id)
);

-- Finished creating all the tables 

-- 5. Add sample of info to view if properly in columns, rows
-- 5.1. Create a ex. user
INSERT INTO users (username, email, password_hash)
VALUES ('alondra', 'alondra@example.com', 'october1031'); -- Creates a user so the posts/trips have a main

-- 5.2. Create a profile for that user
INSERT INTO profiles (user_id, display_name, bio, home_city, home_country)
VALUES (1, 'Alondra', 'Women solo travel & safety tips', 'Chicago', 'USA'); -- profile contains more detailed info

-- 5.3. Destinations that have gone to
INSERT INTO destinations (city, country, region, iso_code)
VALUES 
('Chicago', 'USA', 'Illinois', 'US'),
('Kyoto', 'Japan', 'Kansai', 'JP'),
('Mexico City', 'Mexico', 'CDMX', 'MX'),
('Auckland', 'New Zealand', 'North Island', 'NZ'),
('Wellington', 'New Zealand', 'North Island', 'NZ'),
('Napier', 'New Zealand', 'North Island', 'NZ'),
('Ubud', 'Indonesia', 'Bali', 'ID'),
('Canggu', 'Indonesia', 'Bali', 'ID'),
('Uluwatu', 'Indonesia', 'Bali', 'ID'); -- put travel places so your posts+trips can ref to them

-- 5.4. Insert posts to the aforementioned destinations
INSERT INTO posts (user_id, title, body, rating, is_published, published_at)
VALUES  -- Ex. blog posts by alondra
(1, '48 Hours in Kyoto', 'My tips for solo travel...', 5, true, now()),
(1, 'Solo Adventures in New Zealand’s North Island', 'Trains, ferries, wineries...', 5, true, now()),
(1, 'Finding Healing in Bali', 'Yoga, massages, beaches...', 5, true, now());

-- 5.5. Tags
INSERT INTO tags (name)
VALUES ('solo'), ('food'), ('safety'), ('beach'), ('healing'), ('yoga'), ('culture'), ('adventure');
-- Tags can then support in filtering posts

-- 5.6. Tag each post with correct info (many-to-many)
INSERT INTO post_tags (post_id, tag_id)
SELECT 1, id FROM tags WHERE name IN ('solo', 'food');
INSERT INTO post_tags (post_id, tag_id)
SELECT 2, id FROM tags WHERE name IN ('solo','adventure','culture');
INSERT INTO post_tags (post_id, tag_id)
SELECT 3, id FROM tags WHERE name IN ('healing','yoga','beach'); -- Can link posts to tags for searching

-- 5.7. Posts --> destinations (many-to-many)
INSERT INTO post_destinations (post_id, destination_id)
SELECT 1, id FROM destinations WHERE city = 'Kyoto';
INSERT INTO post_destinations (post_id, destination_id)
SELECT 2, id FROM destinations WHERE city IN ('Auckland','Wellington','Napier');
INSERT INTO post_destinations (post_id, destination_id)
SELECT 3, id FROM destinations WHERE city IN ('Ubud','Canggu','Uluwatu');
-- it allows to fn as connection for posting to 1/+ destination(s)

-- 5.8. + trips
INSERT INTO trips (user_id, destination_id, total_cost, trip_days, safety_score, trip_notes, started_at, ended_at)
SELECT 1, id, 1500.00, 7, 5, 'Great solo trip!' , now() - interval '7 days', now()
FROM destinations WHERE city = 'Kyoto';
INSERT INTO trips (user_id, destination_id, total_cost, trip_days, safety_score, trip_notes, started_at, ended_at)
SELECT 1, id, 2100.00, 14, 5, 'New Zealand biking + ferries.' , now() - interval '14 days', now()
FROM destinations WHERE city = 'Auckland';
INSERT INTO trips (user_id, destination_id, total_cost, trip_days, safety_score, trip_notes, started_at, ended_at)
SELECT 1, id, 1300.00, 10, 4, 'Yoga + massages in Bali.' , now() - interval '10 days', now()
FROM destinations WHERE city = 'Ubud';

