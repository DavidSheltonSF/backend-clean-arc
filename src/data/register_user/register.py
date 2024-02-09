from typing import Type, Dict
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models import Users


class RegisterUser(RegisterUserInterface):
    """RegisterUser use case

    Args:
        RegisterUserInterface (_type_): _description_
    """

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user use case

        Args:
            name (str): User's name
            password (str): User's password

        Returns:
            Dict[bool, users]: Dictionary with imformation of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(name, password)

        return {"Success": validate_entry, "Data": response}
