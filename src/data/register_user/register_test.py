from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser


faker = Faker()


def test_register():
    """Testing registry method"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    # Intance fake data
    attributes = {"name": faker.name(), "password": faker.word()}

    # Insert fake data
    response = register_user.register(attributes["name"], attributes["password"])

    # print(response)

    # testing inputs
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing registry fail method"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    # Intance fake data
    attributes = {"name": faker.random_number(digits=2), "password": faker.word()}

    # Insert fake data
    response = register_user.register(attributes["name"], attributes["password"])

    print(response)

    # testing inputs
    assert not user_repo.insert_user_params  # test if it is {}

    # testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
