from faker import Faker
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel
from src.infra.config import create_database
from .user_repository import UserRepository


create_database()

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """Testing the User repository insert_user method"""

    # Instance the fake dada to insert into Users entity
    user_name = faker.name()
    password = faker.word()

    # Insert the user in database
    new_user = user_repository.insert_user(user_name, password)

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Do a query to select the user fake data from database
    with engine.connect() as conn:
        query_user = conn.execute(
            text(
                f"""
            SELECT *
            FROM users
            WHERE id = {new_user.id}
            """
            )
        ).fetchone()

    # Delete the fake data from database
    with engine.connect() as conn:
        conn.execute(
            text(
                f"""
                DELETE FROM users
                WHERE ID = {new_user.id}
            """
            )
        )
        conn.commit()

    # Check if user data inserted is
    # equal the user data selected by the query
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """Testing the User repository select_user method"""

    # Add fake data into database
    for c in range(2):

        # Intance fake data to insert before selecting
        user_id = faker.random_number(digits=5)
        user_name = faker.name()
        password = faker.word()

        # Instance an User object
        data = UsersModel(id=user_id, name=user_name, password=password)

        # Get the database engine
        engine = db_connection_handler.get_engine()

        # Insert a fake user to test the query selection
        with engine.connect() as conn:
            conn.execute(
                text(
                    f"""
                    INSERT INTO USERS (id, name, password)
                    VALUES ('{user_id}', '{user_name}', '{password}')
                """
                )
            )
            conn.commit()

    # Do 3 query selections to test
    query_user1 = user_repository.select_user(user_id=user_id)
    query_user2 = user_repository.select_user(user_name=user_name)
    query_user3 = user_repository.select_user()  # Return -> List[User]

    # Check if User data inserted
    # is in the data obtained in the queries
    assert data in query_user1
    assert data in query_user2

    # Checking the selection of all users in databae

    # Select all users by engine
    with engine.connect() as conn:
        # Return -> sqlalchemy row sequence
        query_rows = conn.execute(
            text(
                """
                    SELECT * FROM users
                """
            )
        ).fetchall()
        conn.commit()

    # Convert rows from database into User instances
    query_full_data = [UsersModel.row_to_user(row) for row in query_rows]

    # Check if selection by engine is equal selection by repository
    assert all(qfull == q3 for qfull, q3 in zip(query_full_data, query_user3))

    # Delete the fake user from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM users WHERE id='{user_id}'"))
        conn.commit()


def test_update_user():
    """Testing the User repository update_user method"""

    # Intance fake data to insert before updating
    user_id = faker.random_number(digits=5)
    user_name = faker.name()
    password = faker.word()

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Insert a fake user to test the query selection
    with engine.connect() as conn:
        conn.execute(
            text(
                f"""
                INSERT INTO USERS (id, name, password)
                VALUES ('{user_id}', '{user_name}', '{password}')
            """
            )
        )
        conn.commit()

    # Do query uptate to test
    updated_data = user_repository.update_user(
        user_id=user_id, user_name=user_name, password=password
    )

    # Select data by user_id
    selection = user_repository.select_user(user_id=user_id)

    # Check if updated data is equal data selected
    assert updated_data.id == selection[0].id
    assert updated_data.name == selection[0].name
    assert updated_data.password == selection[0].password

    # Delete the fake user from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM users WHERE id='{user_id}'"))
        conn.commit()


def test_update_user_no_result_found():
    """Testing the User repository update_user method"""

    # Intance fake data to insert before updating
    user_id = faker.random_number(digits=5)
    user_name = faker.name()
    password = faker.word()

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Do query uptate to test
    updated_data = user_repository.update_user(
        user_id=user_id, user_name=user_name, password=password
    )

    # Check if updated data is None
    assert updated_data is None

    # Delete the fake user from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM users WHERE id='{user_id}'"))
        conn.commit()


def test_delete_user():
    """Testing the User repository delete_user method"""

    # Intance fake data to insert before deletion
    user_id = faker.random_number(digits=5)
    user_name = faker.name()
    password = faker.word()

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Insert a fake user
    with engine.connect() as conn:
        conn.execute(
            text(
                f"""
                INSERT INTO USERS (id, name, password)
                VALUES ('{user_id}', '{user_name}', '{password}')
            """
            )
        )
        conn.commit()

    # Delete fake user
    deleted_data = user_repository.delete_user(user_id=user_id)

    # Select data by user_id
    selection = user_repository.select_user(user_id=user_id)

    # Check return of delete_user method
    assert deleted_data.id == user_id
    assert deleted_data.name == user_name
    assert deleted_data.password == password

    # Check if deleted data is not in database
    assert not selection

    # Delete the fake user from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM users WHERE id='{user_id}'"))
        conn.commit()


def test_delete_user_no_result_found():
    """Testing the User repository delete_user method"""

    # Intance fake data to insert before deletion
    user_id = faker.random_number(digits=5)

    # Get the database engine
    engine = db_connection_handler.get_engine()

    # Do query uptate to test
    deleted_data = user_repository.delete_user(user_id=user_id)

    # Check if updated data is None
    assert deleted_data is None

    # Delete the fake user from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM users WHERE id='{user_id}'"))
        conn.commit()
