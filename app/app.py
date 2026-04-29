# do not have to run this, will be calling if VENV is active & containter is fning properly
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from week3.app.travel_blog_enhanced.insomnia import bp as posts_bp

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@pg:5432/travel_blog'
from models import db   # import your models
db.init_app(app)
migrate=Migrate(app,db)
app.register_blueprint(posts_bp)

@app.route('/')
def home():
    return {'message': 'Travel Blog API running'}
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
