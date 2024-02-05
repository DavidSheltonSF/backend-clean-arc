from faker import Faker
from src.infra.config import DBConnectionHandler

# from src.infra.entities import Pets as PetsModel
from src.infra.repo import PetRepository
from src.infra.entities import AnimalTypes

faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pet():
    """Shold insert a pet into Pets"""

    # Intance fake data do insert into Pets
    name = faker.name()
    specie = faker.random_element(list(AnimalTypes)).name
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=5)

    # Insert the fake data
    new_pet = pet_repository.insert_pet(
        name=name, specie=specie, age=age, user_id=user_id
    )
    # Get database's enigine
    engine = db_connection_handler.get_engine()

    # Query to select the fake data from database
    query_pet = engine.execute(
        f"""
        SELECT *
        FROM pets
        WHERE ID = {new_pet.id}
        """
    ).fetchone()

    # print(query_pet)
    # print(new_pet)

    # Delete fake data from database
    engine.execute(
        f"""
        DELETE FROM pets
        WHERE ID = {new_pet.id}
        """
    )

    # Check if data inserted is equal data obtained by query
    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id