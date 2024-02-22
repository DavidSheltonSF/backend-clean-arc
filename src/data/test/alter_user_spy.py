from typing import Dict
from src.domain.test import mock_users
from src.domain.models import Users


class AlterUserSpy:
    """Clss to define usecase: Alter User"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository

        self.alter_param = {}

    def alter(
        self,
        user_id: int,
        user_name: str,
        password: str,
    ) -> Dict[bool, Users]:
        """AlterUser use case"""

        self.alter_param["user_id"] = user_id
        self.alter_param["user_name"] = user_name
        self.alter_param["password"] = password

        response = None

        validate_entry = (
            isinstance(user_id, int)
            and isinstance(user_name, str)
            and isinstance(password, str)
        )

        if validate_entry:
            response = mock_users()

        return {"Success": validate_entry, "Data": response}
