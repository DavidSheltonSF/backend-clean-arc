from faker import Faker
from sqlalchemy import text
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
    pet_name = faker.name()
    specie = faker.random_element(list(AnimalTypes)).name
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=5)

    # Insert the fake data
    new_pet = pet_repository.insert_pet(
        pet_name=pet_name, specie=specie, age=age, user_id=user_id
    )

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Do a query to select the pet fake data from database
    with engine.connect() as conn:
        query_pet = conn.execute(
            text(
                f"""
            SELECT *
            FROM pets
            WHERE ID = {new_pet.id}
            """
            )
        ).fetchone()

    # print(query_pet)
    # print(new_pet)

    # Delete the fake data from database
    with engine.connect() as conn:
        conn.execute(
            text(
                f"""
            DELETE FROM pets
            WHERE ID = {new_pet.id}
            """
            )
        )
        conn.commit()

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
    pet_name = faker.name()
    specie = faker.random_element(list(AnimalTypes)).name
    specie_mock = AnimalTypes(specie.lower())
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=5)

    # Instance an Pet object
    data = PetsModel(
        id=pet_id, name=pet_name, specie=specie_mock, age=age, user_id=user_id
    )

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Insert a fake pet to test the query selection
    with engine.connect() as conn:
        conn.execute(
            text(
                f"""
                INSERT INTO pets
                (id, name, specie, age, user_id)
                VALUES
                ('{pet_id}', '{pet_name}', '{specie}', '{age}', '{user_id}')
            """
            )
        )
        conn.commit()

    # Do 3 query selections to test
    query_pet1 = pet_repository.select_pet(pet_id=pet_id)
    query_pet2 = pet_repository.select_pet(user_id=user_id)
    query_pet3 = pet_repository.select_pet()  # Return -> List[User]

    # Check if Pet data inserted
    # is in the data obtained in the queries
    assert data in query_pet1
    assert data in query_pet2

    # Select all pets by engine
    with engine.connect() as conn:
        # Return -> sqlalchemy row sequence
        query_rows = conn.execute(
            text(
                """
                    SELECT * FROM pets
                """
            )
        ).fetchall()
        conn.commit()

    # Convert rows from database into User instances
    query_full_data = [PetsModel.row_to_pet(row) for row in query_rows]

    # Check if selection by engine is equal selection by repository
    assert all(qfull == q3 for qfull, q3 in zip(query_full_data, query_pet3))

    if pet_id:
        # Delete the fake pet from database
        with engine.connect() as conn:
            conn.execute(text(f"DELETE FROM pets WHERE id='{pet_id}'"))
            conn.commit()
    elif user_id:
        # Delete the fake pet from database
        with engine.connect() as conn:
            conn.execute(text(f"DELETE FROM pets WHERE user_id='{user_id}'"))
            conn.commit()


def test_update_pet():
    """Testing the Pet repository update_pet method"""

    # Intance fake data to insert before selecting
    pet_id = faker.random_number(digits=4)
    pet_name = faker.name()
    specie = faker.random_element(list(AnimalTypes)).name
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=5)

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Insert a fake pet to test the query selection
    with engine.connect() as conn:
        conn.execute(
            text(
                f"""
                INSERT INTO pets
                (id, name, specie, age, user_id)
                VALUES
                ('{pet_id}', '{pet_name}', '{specie}', '{age}', '{user_id}')
            """
            )
        )
        conn.commit()

    # Do query uptate to test
    updated_data = pet_repository.update_pet(
        pet_id=pet_id, pet_name=pet_name, specie=specie, age=age
    )

    # Select data by pet_id
    selection = pet_repository.select_pet(pet_id=pet_id)

    # Check if updated data is equal data selected
    assert updated_data.id == selection[0].id
    assert updated_data.name == selection[0].name
    assert updated_data.specie == selection[0].specie.name
    assert updated_data.age == selection[0].age

    # Delete the fake user from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM pets WHERE id='{pet_id}'"))
        conn.commit()


def test_update_pet_no_result_found():
    """Testing the User repository update_user method"""

    # Intance fake data to insert before selecting
    pet_id = faker.random_number(digits=4)
    pet_name = faker.name()
    specie = faker.random_element(list(AnimalTypes)).name
    age = faker.random_number(digits=2)

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Do query uptate to test
    updated_data = pet_repository.update_pet(
        pet_id=pet_id, pet_name=pet_name, specie=specie, age=age
    )

    # Check if updated data is empty
    assert not updated_data

    # Delete the fake user from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM pets WHERE id='{pet_id}'"))
        conn.commit()


def test_delete_pet():
    """Testing the Pet repository delete_pet method"""

    # Intance fake data to insert before deletion
    pet_id = faker.random_number(digits=4)
    pet_name = faker.name()
    specie = faker.random_element(list(AnimalTypes)).name
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=5)

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Insert a fake pet to test the query selection
    with engine.connect() as conn:
        conn.execute(
            text(
                f"""
                INSERT INTO pets
                (id, name, specie, age, user_id)
                VALUES
                ('{pet_id}', '{pet_name}', '{specie}', '{age}', '{user_id}')
            """
            )
        )
        conn.commit()

    # Delete fake pet
    deleted_data = pet_repository.delete_pet(pet_id=pet_id)

    # Select data by pet_id
    selection = pet_repository.select_pet(pet_id=pet_id)

    # Check return of delete_user method
    assert deleted_data.id == pet_id
    assert deleted_data.name == pet_name
    assert deleted_data.specie == specie
    assert deleted_data.age == age
    assert deleted_data.user_id == user_id

    # Check if deleted data is not in database
    assert not selection

    # Delete the fake user from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM pets WHERE id='{pet_id}'"))
        conn.commit()


def test_delete_user_no_result_found():
    """Testing the User repository delete_user method"""

    # Intance fake data to insert before deletion
    pet_id = faker.random_number(digits=5)

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Do query uptate to test
    deleted_data = pet_repository.delete_pet(pet_id=pet_id)

    # Check if updated data is None
    assert deleted_data is None

    # Delete the fake pet from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM pets WHERE id='{pet_id}'"))
        conn.commit()
