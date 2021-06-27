"""Create session Use Case.

This file is reponsible for creating a new session

"""

from datetime import date

from app.session.models.session import Session


class CreateSessionUseCase:
    """Create Session Use Case class."""

    def __init__(self, session_repo, user_repo):
        """Initialize use case class.

        Parameters
            session_repo : SessionRepository
                Session repository

            user_repo : UserRepository
                User repository
        """
        self.session_repo = session_repo
        self.user_repo = user_repo

    def run(self, user_id, start_time):
        """Run create session use case.

        Parameter:
            user_id : int
                user id for the session

            start_time : str
                session start time

        Returns:
            None
        """
        start_datetime = "{0} {1}:00".format(
            date.today().strftime("%Y-%m-%d"), start_time
        )
        user = self.user_repo.get_by_id(user_id)
        session = Session(user=user, start_datetime=start_datetime)

        self.session_repo.add(session)
