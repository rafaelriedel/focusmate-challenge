"""List user Use Case.

This file is reponsible for creating a new session

"""


class ListUserUseCase:
    """List user Use Case class."""

    def __init__(self, user_repo):
        """Initialize use case class.

        Parameters
            user_repo : UserRepository
                User repository
        """
        self.user_repo = user_repo

    def run(self):
        """Return all users.

        Parameter:
            None

        Returns:
            A list of user objects
        """
        return [s.as_dict() for s in self.user_repo.list()]
