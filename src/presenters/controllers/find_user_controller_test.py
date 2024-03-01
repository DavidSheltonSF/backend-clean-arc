from faker import Faker
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_controller import FindUserController

faker = Faker()


def test_route_passing_id():
    """Testing FindUserController route method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(view_args={"user_id": faker.random_number()})

    response = find_user_controller.route(http_request)

    # Testing inputs
    assert (
        find_user_use_case.by_id_param["user_id"] == http_request.view_args["user_id"]
    )

    # Testing outputs
    assert response.status_code == 200
    assert response.body


def test_route_passing_name():
    """Testing FindUserController route method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(view_args={"user_name": faker.name()})

    response = find_user_controller.route(http_request)

    # Testing inputs
    assert (
        find_user_use_case.by_name_param["user_name"]
        == http_request.view_args["user_name"]
    )

    # Testing outputs
    assert response.status_code == 200
    assert response.body


def test_route_passing_nothing():
    """Testing FindUserController route method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest()

    response = find_user_controller.route(http_request)

    # Testing outputs
    assert response.status_code == 200
    assert response.body
