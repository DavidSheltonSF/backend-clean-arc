from faker import Faker
from src.infra.test import UserRepositorySpy
from .alter import AlterUser


faker = Faker()


def test_alter():
    """Testing registry method"""
    user_repo = UserRepositorySpy()
    alter_user = AlterUser(user_repo)

    # Intance fake data
    attributes = {
        "user_id": faker.random_number(digits=5),
        "user_name": faker.name(),
        "password": faker.word(),
    }

    # Update fake user with fake data
    response = alter_user.alter(
        attributes["user_id"], attributes["user_name"], attributes["password"]
    )

    # testing inputs
    assert user_repo.update_user_params["user_id"] == attributes["user_id"]
    assert user_repo.update_user_params["user_name"] == attributes["user_name"]
    assert user_repo.update_user_params["password"] == attributes["password"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_alter_fail():
    """Testing registry method"""
    user_repo = UserRepositorySpy()
    alter_user = AlterUser(user_repo)

    # Intance fake data
    attributes = {
        "user_id": "invalid ID",
        "user_name": faker.name(),
        "password": faker.word(),
    }

    # Update fake user with fake data
    response = alter_user.alter(
        attributes["user_id"], attributes["user_name"], attributes["password"]
    )

    # testing inputs
    assert not user_repo.update_user_params  # test if it is {}

    # testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
