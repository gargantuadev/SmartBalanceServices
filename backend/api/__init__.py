# __init__.py
from flask import Flask
from flask_cors import CORS
#from flask_sqlalchemy import SQLAlchemy

from config.settings import DevelopmentConfig, ProductionConfig
from .categories import categories_bp
#from .db import db

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS
    app.config.from_object(DevelopmentConfig)

    from .models import Base
    from .db import engine
    with app.app_context():
        Base.metadata.create_all(engine)

    app.register_blueprint(categories_bp, url_prefix='/categories')
    #app.register_blueprint(api_bp, url_prefix='/api')  # Register the API blueprint
    return app
