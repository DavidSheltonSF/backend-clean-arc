from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel
from src.infra.repo import PetRepository
from src.infra.entities import AnimalTypes

faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pet():
    """Testing the Pet repository insert_pet method"""

    # Intance fake data do insert into Pets entity
    name = faker.name()
    specie = faker.random_element(list(AnimalTypes)).name
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=5)

    # Insert the fake data
    new_pet = pet_repository.insert_pet(
        name=name, specie=specie, age=age, user_id=user_id
    )

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Do a query to select the pet fake data from database
    query_pet = engine.execute(
        f"""
        SELECT *
        FROM pets
        WHERE ID = {new_pet.id}
        """
    ).fetchone()

    # print(query_pet)
    # print(new_pet)

    # Delete the fake data from database
    engine.execute(
        f"""
        DELETE FROM pets
        WHERE ID = {new_pet.id}
        """
    )

    # Check if pet data inserted is
    # equal the pet data selected by the query
    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id


def test_select_pet():
    """Testing the Pet repository select_pet method"""

    # Intance fake data to insert before selecting
    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = faker.random_element(list(AnimalTypes)).name
    specie_mock = AnimalTypes(specie.lower())
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=5)

    # Instance an Pet object
    data = PetsModel(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Insert a fake pet to test the query selection
    engine.execute(
        f"""
            INSERT INTO pets
            (id, name, specie, age, user_id)
            VALUES
            ('{pet_id}', '{name}', '{specie}', '{age}', '{user_id}')
        """
    )

    # Do 3 query selections to test
    query_pet1 = pet_repository.select_pet(pet_id=pet_id)
    query_pet2 = pet_repository.select_pet(user_id=user_id)
    query_pet3 = pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

    # Check if Pet data inserted
    # is in the data obtained in the queries
    assert data in query_pet1
    assert data in query_pet2
    assert data in query_pet3

    if pet_id:
        # Delete the fake pet from database
        engine.execute(f"DELETE FROM pets WHERE id='{pet_id}'")
    elif user_id:
        # Delete the fake pet from database
        engine.execute(f"DELETE FROM pets WHERE user_id='{user_id}'")
