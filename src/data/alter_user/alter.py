from typing import Type, Dict
from werkzeug.security import generate_password_hash
from src.domain.use_cases import AlterUser as AlterUserInterface
from src.domain.models import Users
from src.infra.repo import UserRepository


class AlterUser(AlterUserInterface):
    """AlterUser use case

    Args:
        RegisterUserInterface (_type_): _description_
    """

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def alter(self, user_id: int, user_name: str, password: str) -> Dict[bool, Users]:
        """Alter user use case

        Args:
            user_id (int): User id
            user_name (str): User name
            password (str): User password

        Returns:
            Dict[bool, Users]: Dictionary with information of the process
        """

        response = None

        validate_entry = (
            isinstance(user_id, int)
            and isinstance(user_name, str)
            and isinstance(password, str)
        )

        if validate_entry:
            response = self.user_repository.update_user(
                user_id=user_id,
                user_name=user_name,
                password=generate_password_hash(password),
            )

        return {"Success": validate_entry, "Data": response}
