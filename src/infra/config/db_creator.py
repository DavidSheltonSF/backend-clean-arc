from .db_base import Base
from .db_config import DBConnectionHandler


def create_database():
    db_conn = DBConnectionHandler()
    engine = db_conn.get_engine()
    Base.metadata.create_all(engine)
