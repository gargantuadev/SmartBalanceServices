# __init__.py
from flask import Flask
from flask_cors import CORS
#from flask_sqlalchemy import SQLAlchemy

from config.settings import DevelopmentConfig, ProductionConfig
#from config.db_config import DATABASE_URL
from .categories import categories_bp
#from .db import db

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS
    app.config.from_object(DevelopmentConfig)

    """app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()"""

    app.register_blueprint(categories_bp, url_prefix='/categories')
    #app.register_blueprint(api_bp, url_prefix='/api')  # Register the API blueprint
    return app
