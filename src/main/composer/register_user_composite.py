from src.main.interface import RouteInterface
from src.infra.repo import UserRepository
from src.data.register_user import RegisterUser
from src.presenters.controllers import RegisterUserController


def register_user_composer() -> RouteInterface:
    """
    Composing Register User Route
    return - Object with User Route
    """
    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
