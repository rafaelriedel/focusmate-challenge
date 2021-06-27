"""User view file.

Flask user view and URL mapping

"""
from . import user_blueprint

from flask.views import MethodView
from flask import make_response, jsonify

from app import db
from app.user.models.repository import UserRepository

from app.user.usecase.list_user import ListUserUseCase


class UserView(MethodView):
    """User view class."""

    def get(self):
        """Get all users.

        Returns:
            JSON user list
        """
        uc = ListUserUseCase(UserRepository(db.session))

        return make_response(jsonify(uc.run()), 200)


user_view = UserView.as_view('user_view')

user_blueprint.add_url_rule('/users', view_func=user_view, methods=['GET'])
