from faker import Faker
from src.data.test import AlterUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .alter_user_controller import AlterUserController

faker = Faker()


def test_route():
    """Testing AlterUserController route method"""

    alter_user_use_case = AlterUserSpy(UserRepositorySpy())
    alter_user_router = AlterUserController(alter_user_use_case)

    attributes = {
        "user_id": faker.random_number(digits=5),
        "user_name": faker.name(),
        "password": faker.name(),
    }

    response = alter_user_router.route(HttpRequest(body=attributes))
    print(response)

    # Testing inputs
    assert alter_user_use_case.alter_param["user_id"] == attributes["user_id"]
    assert alter_user_use_case.alter_param["user_name"] == attributes["user_name"]
    assert alter_user_use_case.alter_param["password"] == attributes["password"]

    # Testing outputs
    assert response.status_code == 200
    assert response.body
    assert "error" not in response.body
