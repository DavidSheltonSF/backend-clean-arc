from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser

faker = Faker()


def test_by_id():
    """Testing Find User use case"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"user_id": faker.random_number(digits=5)}

    # Select user by id:
    response1 = find_user.by_id(attributes["user_id"])

    print(user_repo.select_user_params)
    print(response1)

    # Test inputs
    assert user_repo.select_user_params["user_id"] == attributes["user_id"]

    # Test outputs
    assert response1["Success"] is True
    assert response1["Data"]


def test_by_name():
    """Testing Find User use case"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"name": faker.name()}

    # Select user by name:
    response1 = find_user.by_name(attributes["name"])

    print(user_repo.select_user_params)
    print(response1)

    # Test inputs
    assert user_repo.select_user_params["name"] == attributes["name"]

    # Test outputs
    assert response1["Success"] is True
    assert response1["Data"]


def test_by_id_and_name():
    """Testing Find User use case"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"user_id": faker.random_number(digits=5), "name": faker.name()}

    # Select user by name:
    response1 = find_user.by_id_and_name(attributes["user_id"], attributes["name"])

    print(user_repo.select_user_params)
    print(response1)

    # Test inputs
    assert user_repo.select_user_params["user_id"] == attributes["user_id"]
    assert user_repo.select_user_params["name"] == attributes["name"]

    # Test outputs
    assert response1["Success"] is True
    assert response1["Data"]
