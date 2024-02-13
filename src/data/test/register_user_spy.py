from typing import Dict
from src.domain.test import mock_users
from src.domain.models import Users


class RegisterUserSpy:
    """Spy to RegisterUser use case"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.register_param = {}

    def register(self, user_name: str, password: str) -> Dict[bool, Users]:
        """Register user use case"""

        self.register_param["user_name"] = user_name
        self.register_param["password"] = password

        response = None

        validate_entry = isinstance(user_name, str) and isinstance(password, str)

        if validate_entry:
            response = mock_users()

        return {"Success": validate_entry, "Data": response}
