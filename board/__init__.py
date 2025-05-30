import os
from flask import Flask
from dotenv import load_dotenv
from config import config_by_name
from .models import db 
from . import pages, posts  # import your blueprints


load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Set configuration based on FLASK_ENV
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config_by_name[env])

    # Initialize extensions
    with app.app_context():
        db.init_app(app)
        db.create_all()

    from . import models  # import Post ORM

    # Register blueprints
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)

    # Debug output
    print(f"Running in environment: {env}")
    print(f"DB URL: {app.config.get('SQLALCHEMY_DATABASE_URI')}")

    return app
