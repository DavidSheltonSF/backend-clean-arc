from faker import Faker
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.infra.entities import AnimalTypes
from src.data.test import FindUserSpy
from .register import RegisterPet


faker = Faker()


def test_register():
    """Testing registry method"""
    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy)
    register_pet = RegisterPet(pet_repo, find_user)

    # Intance fake data
    attributes = {
        "name": faker.name(),
        "specie": faker.random_element(list(AnimalTypes)).name,
        "age": faker.random_number(digits=2),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "name": faker.name(),
        },
    }

    # Insert fake data
    response = register_pet.register(
        attributes["name"],
        attributes["specie"],
        attributes["age"],
        attributes["user_information"],
    )

    # testing inputs
    assert pet_repo.insert_pet_params["name"] == attributes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]
    print(pet_repo.insert_pet_params)

    # Testing FindUser Inputs
    assert (
        find_user.by_id_and_name_param["user_id"]
        == attributes["user_information"]["user_id"]
    )
    assert (
        find_user.by_id_and_name_param["name"] == attributes["user_information"]["name"]
    )
    print(find_user.by_id_and_name_param)

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]