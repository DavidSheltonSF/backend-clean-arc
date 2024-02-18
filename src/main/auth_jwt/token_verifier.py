from functools import wraps
from flask import request, jsonify
import jwt
from src.main.auth_jwt.token_handler import token_creator
from src.main.configs.jwt_config_file import jwt_config


def token_verify(func):
    """Decorator to require token to access a route"""

    @wraps(func)
    def decorated(*args, **kwargs):
        """decorated function"""

        # Retrieve raw token and user's id from headers
        raw_token = request.headers.get("Authorization")
        user_id = request.headers.get("User-Id")

        # Check if raw_token is not in request
        if not raw_token:
            return jsonify({"error": "Token is required"}), 401

        # Try decode token
        try:

            # Retrieve token from raw token: "Barear dfd%45344fsa..."
            token = raw_token.split()[1]  # (Barear, dfd%45344fsa...)

            # Decode token
            token_info = jwt.decode(
                jwt=token, key=jwt_config["TOKEN_KEY"], algorithms="HS256"
            )

            # Retrieve user_id from token
            token_user_id = token_info["user_id"]

        except Exception as exc:
            print(exc)
            return jsonify({"error": "ERRORR!!!"}), 401

        # Check if token id is equal the id of
        # the user that is doing the request
        if int(user_id) != token_user_id:
            return jsonify({"error": "User forbidden"}), 400

        # Refresh token if it is ready to refresh
        next_token = token_creator.refresh(token)

        return func(next_token, *args, **kwargs)

    return decorated
