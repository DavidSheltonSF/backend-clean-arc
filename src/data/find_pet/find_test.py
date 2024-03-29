from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import FindPet

faker = Faker()


def test_by_pet_id():
    """Testing Find Pet use case"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    # Fake data
    attributes = {"pet_id": faker.random_number(digits=5)}

    # Select pet by id:
    response = find_pet.by_pet_id(attributes["pet_id"])

    # Test inputs
    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]

    # Test outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_no_pet_id():
    """Testing Find Pet use case"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    # Fake data
    attributes = {"pet_id": None}

    # Select pet by id:
    response = find_pet.by_pet_id(attributes["pet_id"])

    # Test inputs
    assert not pet_repo.select_pet_params

    # Test outputs
    assert response["Success"] is False
    assert not response["Data"]


def test_by_user_id():
    """Testing Find Pet use case"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    # Fake data
    attributes = {"user_id": faker.random_number(digits=5)}

    # Select pet by user_id:
    response = find_pet.by_user_id(attributes["user_id"])

    # Test inputs
    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    # Test outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_user_id_no_user_id():
    """Testing Find Pet use case"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    # Fake data
    attributes = {"user_id": None}

    # Select pet by user_id:
    response = find_pet.by_user_id(attributes["user_id"])

    # Test inputs
    assert not pet_repo.select_pet_params

    # Test outputs
    assert response["Success"] is False
    assert not response["Data"]


def test_all():
    """Testing Find Pet use case"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    # Select pet by user_id:
    response = find_pet.all()

    # Test outputs
    assert response["Success"] is True
    assert response["Data"]
