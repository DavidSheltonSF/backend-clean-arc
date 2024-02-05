import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Define Anymals Types

    Args:
        enum (Enum): _description_
    """

    DOG = "dog"
    CAT = "cat"
    FISH = "fish"
    TURTLE = "turtle"


class Pets(Base):
    """Pets Entity

    Args:
        Base (alias): _description_
    """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):

        return f"""
        Pet [
            name={self.name},
            specie={self.specie},
            userId={self.user_id}
        ]
        """

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.specie == other.specie
            and self.age == other.age
            and self.user_id == other.user_id
        ):
            return True
        return False
