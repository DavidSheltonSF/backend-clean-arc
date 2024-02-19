from .db_base import Base
from .db_config import DBConnectionHandler


def create_database():
    """Create database and tables"""
    db_conn = DBConnectionHandler()
    engine = db_conn.get_engine()
    Base.metadata.create_all(engine)
