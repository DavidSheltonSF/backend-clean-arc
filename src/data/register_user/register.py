from src.domain.use_cases import RegisterUser as RegisterUserInterface


class RegisterUser(RegisterUserInterface):
    """RegisterUser use case

    Args:
        RegisterUserInterface (_type_): _description_
    """

    def __init__(self, user_repository):
        self.user_repository = user_repository
