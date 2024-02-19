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

    # print(query_user)
    # print(new_user)
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
    query_user3 = user_repository.select_user(user_id=user_id, user_name=user_name)

    # Check if User data inserted
    # is in the data obtained in the queries
    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    # Delete the fake user from database
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM users WHERE id='{user_id}'"))
        conn.commit()
