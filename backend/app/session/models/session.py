"""Session model file."""
from app import db
from app.user.models.user import User


class Session(db.Model):
    """Session model class."""

    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    start_datetime = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship("User")

    def as_dict(self):
        """Return a dict version.

        Returns
            dict
        """
        return {
            'id': self.id,
            'user': self.user.as_dict(keys=['id', 'email', 'first_name', 'last_name']),
            'start_datetime': self.start_datetime,
        }
