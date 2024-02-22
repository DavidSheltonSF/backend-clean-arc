from src.infra.repo import UserRepository
from src.data.alter_user import AlterUser
from src.presenters.controllers import AlterUserController


def alter_user_composer() -> AlterUserController:
    """
    Composing Alter User Route
    return - Object with User Route
    """
    repository = UserRepository()
    use_case = AlterUser(repository)
    alter_user_route = AlterUserController(use_case)

    return alter_user_route
