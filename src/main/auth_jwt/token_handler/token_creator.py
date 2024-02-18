from datetime import datetime, timedelta
import jwt
import time


class TokenCreator:
    """Class to create and refresh token"""

    def __init__(self, token_key: str, exp_time_min: int, refresh_time_min: int):

        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min
        self.__REFRESH_TIME_MIN = refresh_time_min

    def create(self, user_id: int) -> str:
        """Create a token for an user, using his id
        Args:
            uid (int): User's id

        Returns:
            str: Token for a user
        """
        return self.__encode(user_id)

    def refresh(self, token: str) -> str:
        """Refresh a token if it is going to expire

        Args:
            token (str): Token to refresh

        Returns:
            str: The token refreshed
        """
        # Decode token
        token_info = jwt.decode(jwt=token, key=self.__TOKEN_KEY, algorithms="HS256")

        # Retreave user's id and expiration time from token
        user_id = token_info["user_id"]
        exp_time = token_info["exp"]

        # Check if token is going to expire
        if ((exp_time - time.time()) / 60) < self.__REFRESH_TIME_MIN:
            return self.__encode(user_id)

        return token

    def __encode(self, user_id: int) -> str:
        """Encode a token using user's id and return it

        Args:
            user_id (int): User's id

        Returns:
            str: Token for a user
        """
        token = jwt.encode(
            payload={
                "exp": datetime.utcnow() + timedelta(minutes=self.__EXP_TIME_MIN),
                "user_id": user_id,
            },
            key=self.__TOKEN_KEY,
            algorithm="HS256",
        )
        return token
