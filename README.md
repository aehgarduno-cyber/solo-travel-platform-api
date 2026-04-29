1- Travel Blog for Solo Women Travelers

2- Overview
A safe, empowering space to share ones adventures, tips & cultural experiences. This project is a full-stack Flask & PostgreSQL app designed to help women solo travelers to have a space to share travel blogs, track trips, explore new destinations & find safety tips/tricks.

The system includes:
-A relational PostgreSQL database
-SQLAlchemy ORM models
-Flask REST API endpoints
-Sample data for sample destinations (Japan, Mexico, Chicago, New Zealand, Bali)

3- Features
Create, read, update& delete (CRUD) blog posts
Track trips:
-cost
-days
-safety score
-notes

4- ER Diagram
1:1 --> users --> profiles
1:many --> users --> posts
many:many --> posts <--> tags
many:many --> posts <--> destinations
1:many --> destinations --> trips

5- Database Setup
-Run inside pgAdmin:
--Run schema.sql
--Run seed.sql
-Running Flask (inside flask_container VENV)
--source venv/bin/activate
--pip install -r requirements.txt
--flask run --host=0.0.0.0 --port=5000Show more lines
--Your API is now live at:
--http://localhost:5000

6- API Reference
POST /users    || Create a new user
GET /posts     || Returns all posts
GET /posts/    || Returns one post
POST /posts    || Create a post
PUT /posts/    || Update a post
DELETE /posts/ || Delete a post

7- Potential Improvements
-If an index is added: SQLCREATE then idx_post_destinations_destination_idON post_destinations(destination_id) would show more lines that will help w/ filtering possibly.

8- Visualization 
-Average trip cost per country which helps fellow travelers to track patterns. 

9- Retrospective
-How did the design evolve?
--Started as a travel blog focused & tailored for women (as a fellow solo women traveler I could have benefited from this), expanded into a relational system with posts, trips, destinations, tags.
-ORM or Raw SQL?
--I went with ORM in hope of a cleaner code, using queries & in relation to the mapping of ER diagram.
-Challenges
--Mapping many-to-many tables, definitely trying to successfuly do the configuration of Flask-Migrate, then added a layer of more difficulty trying to troubleshoot Colab. Testing was nice to see new understandings, I still am not entirely sure if it works properly as I envisioned. 

--The improvements that can be added would be more user friendly & addressing similarities to other apps in the market such as comments & likes, creating groups of likeminded people to travel together. Having a duo autentication to protect personal information. 

# Travel Blog Backend API (DevOps Portfolio Project)

## Overview
This project is a backend REST API built with Flask and PostgreSQL to manage travel posts, destinations, trips, and tags. The application is designed for solo travelers to share experiences, track trips, and analyze travel patterns.

The project is being developed as part of the **Modern Software Engineering with DevOps** course, with a focus on containerization, orchestration, and deployment using Docker and Docker Compose.

---

## Current Features
- Flask-based REST API
- PostgreSQL relational database
- CRUD endpoints for travel posts
- Support for destinations, tags, and trips
- SQL schema and seed data included

---

## Project Architecture
The application follows a **2-tier architecture**:
1. **Web Tier**: Flask application exposing REST API endpoints
2. **Data Tier**: PostgreSQL database

These tiers are defined and managed using Docker Compose.

---

## Technologies Used
- Python
- Flask
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose

---

## Current Project Status (Week 2)
At this stage of the project:
- Flask application code has been started
- Database schema and seed data are defined
- Dockerfile has been created for the Flask application
- docker-compose.yml defines Flask and PostgreSQL services
- The project has been pushed to a public GitHub repository

The application is still under development and is not yet fully containerized or deployed.

---

## Planned Enhancements
- Complete Docker Compose configuration
- Database migrations using Flask-Migrate
- Automated tests
- CI/CD pipeline using GitHub Actions
- Cloud deployment using a major cloud provider

---

## How to Run Locally (Development)
```bash
docker-compose up --build

## DevOps Portfolio – Week 2 Status

This repository represents the early stages of a containerized backend
application built as part of the Modern Software Engineering with DevOps course.

At this stage:
- Flask backend code has been added
- PostgreSQL schema and seed data are included
- A Dockerfile has been created for the web service
- docker-compose.yml defines a multi-container architecture
- The project has been pushed to a public GitHub repository

The application is still under development and not yet fully containerized
or deployed.