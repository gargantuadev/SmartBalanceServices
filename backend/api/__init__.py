# __init__.py
from flask import Flask
from flask_cors import CORS
from config.settings import DevelopmentConfig, ProductionConfig
from .categories import categories_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(categories_bp, url_prefix='/api')
    #app.register_blueprint(api_bp, url_prefix='/api')  # Register the API blueprint
    return app
