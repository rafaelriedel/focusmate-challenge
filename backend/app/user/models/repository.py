"""User repository.

This file is responsible for data access methods

"""

from app.user.models.user import User


class UserRepository:
    """User Repository class."""

    def __init__(self, session):
        """Initialize session repository.

        Parameters
            session : SQLAlchemy DB Session
                Database session
        """
        self.session = session

    def add(self, user):
        """Add new user object.

        Parameters:
            user : User object
                user object that will be created

        Returns:
            None
        """
        self.session.add(user)

    def get_by_id(self, id):
        """Get user by its ID.

        Parameters:
            id : int
                user primary key

        Returns:
            Session model object
        """
        return self.session.query(User).filter_by(id=id).one()

    def list(self):
        """Get all users on database.

        Parameters:
            None

        Returns:
            List of users
        """
        return self.session.query(User).all()
