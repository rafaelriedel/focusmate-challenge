"""Session repository.

This file is responsible for data access methods

"""
from app.session.models.session import Session


class SessionRepository:
    """Session Repository class."""

    def __init__(self, session):
        """Initialize session repository.

        Parameters
            session : SQLAlchemy DB Session
                Database session
        """
        self.session = session

    def add(self, session):
        """Add new session model.

        Parameters:
            session : Session model
                session model object that will be created

        Returns:
            None
        """
        self.session.add(session)
        self.session.commit()

    def get_by_id(self, id):
        """Get session by its ID.

        Parameters:
            id : int
                session primary key

        Returns:
            Session model object
        """
        return self.session.query(Session).filter_by(id=id).one()

    def list(self):
        """Get all sessions on database.

        Parameters:
            None

        Returns:
            List of session
        """
        return self.session.query(Session).all()
