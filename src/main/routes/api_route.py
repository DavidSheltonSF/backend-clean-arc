from flask import Blueprint, jsonify

# from src.main.composer import register_user_composer

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api", methods=["GET"])
def something():
    """test"""

    return jsonify({"Programador": "David"})
