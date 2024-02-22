from faker import Faker
from src.data.test import RemoveUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .remove_user_controller import RemoveUserController

faker = Faker()


def test_route():
    """Testing RemoveUserController route method"""

    remove_user_use_case = RemoveUserSpy(UserRepositorySpy())
    remove_user_router = RemoveUserController(remove_user_use_case)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = remove_user_router.route(HttpRequest(body=attributes))

    # Testing inputs
    assert remove_user_use_case.remove_param["user_id"] == attributes["user_id"]

    # Testing outputs
    assert response.status_code == 200
    assert response.body
    assert "error" not in response.body
