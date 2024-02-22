from faker import Faker
from src.infra.test import UserRepositorySpy
from .remove import RemoveUser


faker = Faker()


def test_alter():
    """Testing registry method"""
    user_repo = UserRepositorySpy()
    remove_user = RemoveUser(user_repo)

    # Intance fake data
    attributes = {
        "user_id": faker.random_number(digits=5),
    }

    # Update fake user with fake data
    response = remove_user.remove(attributes["user_id"])

    # testing inputs
    assert user_repo.delete_user_params["user_id"] == attributes["user_id"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_alter_fail():
    """Testing registry method"""
    user_repo = UserRepositorySpy()
    remove_user = RemoveUser(user_repo)

    # Intance fake data
    attributes = {"user_id": "invalid ID"}

    # Update fake user with fake data
    response = remove_user.remove(attributes["user_id"])

    # testing inputs
    assert not user_repo.delete_user_params  # test if it is {}

    # testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
