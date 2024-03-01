from faker import Faker
from src.data.test import FindPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_pet_controller import FindPetController

faker = Faker()


def test_route_passing_pet_id():
    """Testing FindPetController route method"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest(view_args={"pet_id": faker.random_number(digits=2)})

    response = find_pet_controller.route(http_request)

    # Testing inputs
    assert (
        find_pet_use_case.by_pet_id_param["pet_id"] == http_request.view_args["pet_id"]
    )

    # Testing outputs
    assert response.status_code == 200
    assert response.body


def test_route_passing_user_id():
    """Testing FindPetController route method"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest(view_args={"user_id": faker.random_number(digits=5)})

    response = find_pet_controller.route(http_request)

    # Testing inputs
    assert (
        find_pet_use_case.by_user_id_param["user_id"]
        == http_request.view_args["user_id"]
    )

    # Testing outputs
    assert response.status_code == 200
    assert response.body


def test_route_passing_nothing():
    """Testing FindPetController route method"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest()

    response = find_pet_controller.route(http_request)

    # Testing outputs
    assert response.status_code == 200
    assert response.body
