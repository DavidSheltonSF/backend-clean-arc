from typing import List
from sqlalchemy.exc import NoResultFound
from src.data.interfaces import UserRepositoryInterface
from src.domain.models import Users
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, user_name: str, password: str) -> Users:
        """Insert data in user entity

        Args:
            user_nameme (str): user name
            password (str): user password

        Return:
            (NamedTuple => Users): Returns the inserted user data
        """

        # Open database connection and try to add a new user
        with DBConnectionHandler() as db_connection:
            # Try add a new user
            try:
                new_user = UsersModel(name=user_name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                db_connection.session.close()
                raise

    @classmethod
    def select_user(cls, user_id: int = None, user_name: str = None) -> List[Users]:
        """Select data in user entity by id and/or name

        Args:
            user_id (int, optional): Id of the registry. Defaults to None.
            user_name (str, optional): User's name. Defaults to None.

        Returns:
            List[Users]: List with Users selected data
        """

        query_data = None

        # Try select users in database
        try:
            with DBConnectionHandler() as db_connection:
                # Check if has id but has not name
                if user_id and not user_name:

                    # select user by id and get one
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]

                # Check if has not id but has name
                elif not user_id and user_name:

                    # select user by name and get one
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=user_name)
                        .all()
                    )
                    query_data = data

                # Check if has not id or name
                elif not user_id and not user_name:

                    # select user by id and by name, and get one
                    data = db_connection.session.query(UsersModel).all()
                    query_data = data

                return query_data

        # If no user was founded
        except NoResultFound:
            return []

        except:
            db_connection.session.rollback()
            db_connection.session.close()
            raise

    @classmethod
    def update_user(cls, user_id: int, user_name: str, password: str) -> Users:
        """Update data in user entity

        Args:
            use_id (int): user name

        Return:
            (NamedTuple => Users): Returns the updated user data
        """

        with DBConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(UsersModel).filter_by(id=user_id).one()
                )
                user.name = user_name
                user.password = password
                db_connection.session.commit()
                return Users(id=user_id, name=user_name, password=password)

            except NoResultFound:
                return None

            except:
                db_connection.session.rollback()
                db_connection.session.close()
                raise

    @classmethod
    def delete_user(cls, user_id: int) -> Users:
        """Delete data in user entity

        Args:
            use_id (int): user id

        Return:
            (NamedTuple => Users): Returns the deleted user data
        """
        try:
            with DBConnectionHandler() as db_connection:
                user = (
                    db_connection.session.query(UsersModel).filter_by(id=user_id).one()
                )
                db_connection.session.delete(user)
                db_connection.session.commit()

            return Users(id=user.id, name=user.name, password=user.password)

        except NoResultFound:
            return None

        except:
            db_connection.session.rollback()
            db_connection.session.close()
            raise
