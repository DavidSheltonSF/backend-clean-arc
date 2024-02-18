from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer
from src.main.composer import register_pet_composer
from src.main.composer import find_user_composer
from src.main.composer import find_pet_composer
from src.main.adapter import flask_adapter
from src.main.auth_jwt import token_creator, token_verify

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/secret", methods=["GET"])
@token_verify
def secret_route(token):
    """_summary_"""
    return jsonify({"sucess": "Secret DATA!!!", "token": token}), 200


@api_routes_bp.route("/api/auth", methods=["POST"])
def authentification():
    """_summary_"""
    token = token_creator.create(user_id=12)

    return jsonify({"token": token}), 200


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """Register user route"""
    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "Type": "users",
            "id": response.body.id,
            "attributes": {"user_name": response.body.name},
        }
        return jsonify({"data": message}), response.status_code
    # Handling Erros

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["POST"])
def register_pet():
    """Register pet route"""
    message = {}
    response = flask_adapter(request=request, api_route=register_pet_composer())

    if response.status_code < 300:
        message = {
            "Type": "pets",
            "id": response.body.id,
            "attributes": {
                "pet_name": response.body.name,
                "specie": response.body.specie,
                "age": response.body.age,
            },
            "relationships": {"owner": {"type": "users", "id": response.body.user_id}},
        }
        return jsonify({"data": message}), response.status_code
    # Handling Erros

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/users", methods=["GET"])
def find_user():
    """Find user route"""
    message = {}
    response = flask_adapter(request=request, api_route=find_user_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "user",
                    "id": element.id,
                    "attributes": {"user_name": element.name},
                }
            )

        return jsonify({"data": message}), response.status_code

    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/pets", methods=["GET"])
def find_pet():
    """Find pet route"""
    message = {}
    response = flask_adapter(request=request, api_route=find_pet_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "pet",
                    "id": element.id,
                    "attributes": {"pet_name": element.name, "age": element.age},
                    "relationships": {"user_id": element.user_id},
                }
            )

        return jsonify({"data": message}), response.status_code

    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )
