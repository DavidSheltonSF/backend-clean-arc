from functools import wraps
from flask import request, jsonify
import jwt
from src.main.auth_jwt.token_handler import token_creator
from src.main.configs.jwt_config_file import jwt_config


def token_verify(func):
    """_summary"""

    @wraps(func)
    def decorated(*args, **kwargs):
        """_summary"""

        raw_token = request.headers.get("Authorization")
        user_id = request.headers.get("User-Id")

        # Check if raw_token is not in request
        if not raw_token:
            return jsonify({"error": "Token is required"}), 401

        # Try decode token
        try:

            # Retrieve token from raw token: "Barear dfd%45344fsa..."
            token = raw_token.split()[1]  # (Barear, dfd%45344fsa...)
            token_info = jwt.decode(
                jwt=token, key=jwt_config["TOKEN_KEY"], algorithms="HS256"
            )
            token_user_id = token_info["user_id"]
            print(token_info)

        except Exception as exc:
            print(exc)
            return jsonify({"error": "ERRORR!!!"}), 401

        if int(user_id) != token_user_id:
            return jsonify({"error": "User forbidden"}), 400

        next_token = token_creator.refresh(token)

        return func(next_token, *args, **kwargs)

    return decorated
