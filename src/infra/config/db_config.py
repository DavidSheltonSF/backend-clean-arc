from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Class that deals directily with database"""

    def __init__(self):
        self.__connection_string = "sqlite:///storage.sqlite"
        self.session = None

    def get_engine(self):
        """Return connection Engine
        Returns:
            DBConnectionHandler: Engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        """An magic method which the 'with' statement will
        use to OPEN the session
        """
        # Create the database's engine make a session
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """An magic method which the 'with' statement will
        use to CLOSE the session
        """
        self.session.close()
