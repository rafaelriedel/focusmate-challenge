"""Session view file.

Flask user view and URL mapping

"""

from . import session_blueprint

from flask.views import MethodView
from flask import make_response, request, jsonify

from app import db
from app.session.models.repository import SessionRepository
from app.user.models.repository import UserRepository
from app.session.usecase.create_session import CreateSessionUseCase
from app.session.usecase.list_session import ListSessionUseCase


class SessionView(MethodView):
    """User view class."""

    def post(self):
        """Create a new session.

        Returns:
            None
        """
        uc = CreateSessionUseCase(
            SessionRepository(db.session), UserRepository(db.session)
        )

        data = request.get_json()

        uc.run(data.get("user_id"), data.get("start_time"))

        return make_response(jsonify({"message": "object created"}), 200)

    def get(self):
        """Get all sessions.

        Returns:
            JSON session list
        """
        uc = ListSessionUseCase(SessionRepository(db.session))

        return make_response(jsonify(uc.run()), 200)


session_view = SessionView.as_view('session_view')

session_blueprint.add_url_rule(
    '/session', view_func=session_view, methods=['GET', 'POST']
)
