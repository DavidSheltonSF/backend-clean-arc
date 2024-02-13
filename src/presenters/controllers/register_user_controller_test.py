from faker import Faker
from src.infra.test import UserRepositorySpy
from src.data.test import RegisterUserSpy
from src.presenters.helpers import HttpRequest
from .register_user_controller import RegisterUserController

faker = Faker()


def test_route():
    """Testing RegisterUserController"""
    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_controller = RegisterUserController(register_user_use_case)

    attributes = {"user_name": faker.name(), "password": faker.word()}

    http_request = HttpRequest(body=attributes)

    response = register_user_controller.route(http_request)

    print(register_user_use_case.register_param)
    print(response)

    # Testing inputs
    assert register_user_use_case.register_param["user_name"] == attributes["user_name"]
    assert register_user_use_case.register_param["password"] == attributes["password"]

    # Testing outputs
