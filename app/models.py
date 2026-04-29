from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

# User
class User(db.Model): # will map the SQL table 
    __tablename__='users' #user will help link class to the SQL
    id=db.Column(db.BigInteger, primary_key=True)
    username=db.Column(db.String, unique=True, nullable=False)
    email=db.Column(db.String, unique=True, nullable=False)
    password_hash=db.Column(db.Text, nullable=False)
    posts=db.relationship("Post", backref="author") #then this, relationship-post --> connects user --> post w/o SQL
    profile=db.relationship("Profile", backref="user",uselist=False)
    trips=db.relationship("Trip", backref="traveler")

# profilees
class Profile(db.Model):
    __tablename__='profiles'
    id=db.Column(db.BigInteger, primary_key=True)
    user_id=db.Column(db.BigInteger, db.ForeignKey('users.id'))
    display_name=db.Column(db.Text)
    bio=db.Column(db.Text)
    home_city=db.Column(db.Text)
    home_country= db.Column(db.Text)
    avatar_url=db.Column(db.Text)

# destinations
class Destination(db.Model):
    __tablename__='destinations'
    id=db.Column(db.BigInteger, primary_key=True)
    city=db.Column(db.Text)
    country=db.Column(db.Text)
    region=db.Column(db.Text)
    iso_code=db.Column(db.Text)
    trips=db.relationship("Trip", backref="place")

# Posts
class Post(db.Model):
    __tablename__= 'posts'
    id=db.Column(db.BigInteger, primary_key=True)
    user_id=db.Column(db.BigInteger, db.ForeignKey('users.id'))
    title=db.Column(db.Text, nullable=False)
    body=db.Column(db.Text, nullable=False)
    rating=db.Column(db.Integer)
    is_published=db.Column(db.Boolean, default=False)
    destinations=db.relationship(
        "PostDestination",
        backref="post",
        cascade="all, delete-orphan"
    )
    tags=db.relationship(
        "PostTag",
        backref="post",
        cascade="all, delete-orphan"
    )

# Tags
class Tag(db.Model):
    __tablename__ ='tags'
    id=db.Column(db.BigInteger, primary_key=True)
    name=db.Column(db.Text, unique=True)

class PostTag(db.Model):
    __tablename__='post_tags'
    post_id=db.Column(db.BigInteger, db.ForeignKey('posts.id'), primary_key=True)
    tag_id=db.Column(db.BigInteger, db.ForeignKey('tags.id'), primary_key=True)
class PostDestination(db.Model):
    __tablename__='post_destinations'
    post_id=db.Column(db.BigInteger, db.ForeignKey('posts.id'), primary_key=True)
    destination_id=db.Column(db.BigInteger, db.ForeignKey('destinations.id'), primary_key=True)

# Trips, forgot to include this, came back to add 
class Trip(db.Model):
    __tablename__='trips'
    id =db.Column(db.BigInteger, primary_key=True)
    user_id=db.Column(db.BigInteger, db.ForeignKey('users.id'))
    destination_id=db.Column(db.BigInteger, db.ForeignKey('destinations.id'))
    total_cost=db.Column(db.Numeric)
    trip_days=db.Column(db.Integer)
    safety_score=db.Column(db.Integer)
    trip_notes=db.Column(db.Text)
    started_at=db.Column(db.DateTime)
    ended_at=db.Column(db.DateTime)