# __init__.py
from flask import Flask
from flask_cors import CORS
from .routes import api_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS
    app.register_blueprint(api_bp, url_prefix='/api')  # Register the API blueprint
    return app
