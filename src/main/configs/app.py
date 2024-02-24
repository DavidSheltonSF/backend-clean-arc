from flask import Flask
from flask_cors import CORS
from src.main.routes import api_routes_bp
from src.main.caching import cache

app = Flask(__name__)
cache.init_app(app)
CORS(app)

app.register_blueprint(api_routes_bp)
