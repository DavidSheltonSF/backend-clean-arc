from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer
from src.main.composer import register_pet_composer
from src.main.composer import find_user_composer
from src.main.composer import find_pet_composer
from src.main.composer import alter_user_composer
from src.main.composer import alter_pet_composer
from src.main.composer import remove_user_composer
from src.main.composer import remove_pet_composer
from src.main.adapter import flask_adapter
from src.main.auth_jwt import token_creator, token_verify
from src.main.caching import cache


api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/auth", methods=["POST"])
def authentification():
    """Authentification route"""

    # Retrieve user information from body
    user_info = request.get_json()

    # Key to cache token
    key = f"Token: User(id={user_info['user_id']}"

    # Check if token is cached
    if cache.get(key):
        return jsonify({"token": cache.get(key)}), 200

    # Get user data from database
    response = flask_adapter(
        request=request,
        api_route=find_user_composer(),
    )

    # Check if response have a body
    if response.body:

        # Create a token using user id
        token = token_creator.create(user_id=user_info["user_id"])

        # Cache token
        cache.set(key, token)

        return jsonify({"token": token}), 200

    return jsonify({"Error": "user not found"}), 400


@api_routes_bp.route("/api/users", methods=["POST"])
# @token_verify
def register_user():
    """Register user route"""
    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    # Check that an error has not occurred
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
@token_verify
def register_pet(token):
    """Register pet route"""
    message = {}
    response = flask_adapter(request=request, api_route=register_pet_composer())

    # Check that an error has not occurred
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
# @token_verify
def find_user():
    """Find user route"""
    message = {}

    user = {"user_id": None, "user_name": ""}

    # Retrieve query params from request
    data = request.args.to_dict()

    # Update user dictionary
    user.update(data)

    key = f"User(id={user['user_id']}, name={user['user_name']})"

    response = cache.get(key)

    if not response:
        response = flask_adapter(request=request, api_route=find_user_composer())

    # Check that an error has not occurred
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

        cache.set(key, response)
        return jsonify({"data": message}), response.status_code

    # Handling Erros
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/pets", methods=["GET"])
@token_verify
def find_pet(token):
    """Find pet route"""
    message = {}

    pet = {"pet_id": 0, "user_id": 0}

    data = request.args.to_dict()

    pet.update(data)

    key = f"Pet(id={pet['pet_id']}, user_id={pet['user_id']})"

    response = cache.get(key)

    if not response:
        response = flask_adapter(request=request, api_route=find_pet_composer())

    # Check that an error has not occurred
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

        if not cache.get(key):
            cache.set(key, response)

        return jsonify({"data": message}), response.status_code

    # Handling Erros
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/users", methods=["PUT"])
@token_verify
def alter_user(token):
    """Find user route"""
    message = {}
    response = flask_adapter(request=request, api_route=alter_user_composer())
    print(request.get_json())
    # Check that an error has not occurred
    if response.status_code < 300:

        if response.body:

            message = {
                "type": "user",
                "id": response.body.id,
                "attributes": {"user_name": response.body.name},
            }

        return jsonify({"data": message}), response.status_code

    # Handling Erros
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/pets", methods=["PUT"])
@token_verify
def alter_pet(token):
    """Find pet route"""
    message = {}
    response = flask_adapter(request=request, api_route=alter_pet_composer())
    print(request.get_json())
    # Check that an error has not occurred
    if response.status_code < 300:

        if response.body:

            message = {
                "type": "pet",
                "id": response.body.id,
                "attributes": {
                    "pet_name": response.body.name,
                    "specie": response.body.specie,
                    "age": response.body.age,
                },
                "relationships": {"user_id": response.body.user_id},
            }

        return jsonify({"data": message}), response.status_code

    # Handling Erros
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/users", methods=["DELETE"])
@token_verify
def remove_user(tonken):
    """Remove user route"""
    message = {}
    response = flask_adapter(request=request, api_route=remove_user_composer())

    # Check that an error has not occurred
    if response.status_code < 300:

        if response.body:

            message = {
                "type": "user",
                "id": response.body.id,
                "attributes": {"user_name": response.body.name},
            }

        return jsonify({"data": message}), response.status_code

    # Handling Erros
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/pets", methods=["DELETE"])
@token_verify
def remove_pet(token):
    """Find pet route"""
    message = {}
    response = flask_adapter(request=request, api_route=remove_pet_composer())

    # Check that an error has not occurred
    if response.status_code < 300:

        if response.body:

            message = {
                "type": "pet",
                "id": response.body.id,
                "attributes": {
                    "pet_name": response.body.name,
                    "specie": response.body.specie,
                    "age": response.body.age,
                },
                "relationships": {"user_id": response.body.user_id},
            }

        return jsonify({"data": message}), response.status_code

    # Handling Erros
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )
