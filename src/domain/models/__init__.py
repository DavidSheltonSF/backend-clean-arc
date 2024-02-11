"""
    This module contains models to return data
    of an User or a Pet without to use an entity class

    - Each model is an named tuple that can be returned for
    a repository or an use case instead an entity instance;

    - It ensures the data integrity.
"""

from .users import Users
from .pets import Pets
