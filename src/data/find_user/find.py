from typing import Type, Dict, List
from src.domain.use_cases import FindUser as FindUserInterface
from src.infra.repo import UserRepository
from src.domain.models import Users


class FindUser(FindUserInterface):
    """Class to define use case Find User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Find user by id

        Args:
            user_id (int): User's id

        Returns:
            Dict[bool, List[Users]]:
            A response {'Sucess': True/False, 'Data': List[Users]/None}
        """

        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, user_name: str) -> Dict[bool, List[Users]]:
        """Find user by name

        Args:
            user_name (str): User's name

        Returns:
            Dict[bool, List[Users]]:
            A response {'Sucess': True/False, 'Data': List[Users]/None}
        """

        response = None

        validate_entry = isinstance(user_name, str)

        if validate_entry:
            response = self.user_repository.select_user(user_name=user_name)

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[Users]]:
        """Find all users

        Returns:
            Dict[bool, List[Users]]:
            A response {'Sucess': True/False, 'Data': List[Users]/None}
        """

        response = self.user_repository.select_user()

        return {"Success": True, "Data": response}
