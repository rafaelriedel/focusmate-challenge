"""User model file."""
from app import db


class User(db.Model):
    """User model class."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    active = db.Column(db.String(50))
    confirmed = db.Column(db.Boolean, default=False)
    date_confirmed = db.Column(db.DateTime)
    hash_password = db.Column(db.String(1000))

    def as_dict(self, keys=[]):
        """Return a dict version.

        Returns
            dict
        """
        data = {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_created': self.date_created,
            'date_confirmed': self.date_confirmed,
            'confirmed': self.confirmed,
            'active': self.active,
        }

        if keys:
            return {k: v for k, v in data.items() if k in keys}
        else:
            return data
