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

    # Test inputs
    assert user_repo.select_user_params["user_id"] == attributes["user_id"]

    # Test outputs
    assert response1["Success"] is True
    assert response1["Data"]


def test_by_id_no_id():
    """Testing Find User use case by_id method, but passing no id"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"user_id": None}

    # Select user by id:
    response1 = find_user.by_id(attributes["user_id"])

    # Test inputs
    assert not user_repo.select_user_params

    # Test outputs
    assert response1["Success"] is False
    assert not response1["Data"]


def test_by_name():
    """Testing Find User use case"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"user_name": faker.name()}

    # Select user by name:
    response1 = find_user.by_name(attributes["user_name"])

    # Test inputs
    assert user_repo.select_user_params["user_name"] == attributes["user_name"]

    # Test outputs
    assert response1["Success"] is True
    assert response1["Data"]


def test_by_name_no_name():
    """Testing Find User use case"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"user_name": None}

    # Select user by name:
    response1 = find_user.by_name(attributes["user_name"])

    # Test inputs
    assert not user_repo.select_user_params

    # Test outputs
    assert response1["Success"] is False
    assert not response1["Data"]


def test_by_id_and_name():
    """Testing Find User use case"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"user_id": faker.random_number(digits=5), "user_name": faker.name()}

    # Select user by name:
    response1 = find_user.by_id_and_name(attributes["user_id"], attributes["user_name"])

    # Test inputs
    assert user_repo.select_user_params["user_id"] == attributes["user_id"]
    assert user_repo.select_user_params["user_name"] == attributes["user_name"]

    # Test outputs
    assert response1["Success"] is True
    assert response1["Data"]


def test_by_id_and_name_no_id():
    """Testing Find User use case"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"user_id": None, "user_name": faker.name()}

    # Select user by name:
    response1 = find_user.by_id_and_name(attributes["user_id"], attributes["user_name"])

    # Test inputs
    assert not user_repo.select_user_params
    assert not user_repo.select_user_params

    # Test outputs
    assert response1["Success"] is False
    assert not response1["Data"]


def test_by_id_and_name_no_name():
    """Testing Find User use case"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"user_id": faker.random_number(digits=5), "user_name": None}

    # Select user by name:
    response1 = find_user.by_id_and_name(attributes["user_id"], attributes["user_name"])

    # Test inputs
    assert not user_repo.select_user_params
    assert not user_repo.select_user_params

    # Test outputs
    assert response1["Success"] is False
    assert not response1["Data"]


def test_by_id_and_name_no_name_or_id():
    """Testing Find User use case"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    # Fake data
    attributes = {"user_id": None, "user_name": None}

    # Select user by name:
    response1 = find_user.by_id_and_name(attributes["user_id"], attributes["user_name"])

    # Test inputs
    assert not user_repo.select_user_params
    assert not user_repo.select_user_params

    # Test outputs
    assert response1["Success"] is False
    assert not response1["Data"]
