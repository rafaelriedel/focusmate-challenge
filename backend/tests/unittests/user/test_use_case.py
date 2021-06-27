"""Test User use case."""
from unittest.mock import MagicMock
from unittest.mock import Mock

from app.user.models.repository import UserRepository
from app.user.models.user import User
from app.user.usecase.list_user import ListUserUseCase


def test_use_case_list_user():
    """Teste list user."""
    db_session = MagicMock()
    session_list = [Mock(), Mock(), Mock()]
    db_session.query(User).all.return_value = session_list

    uc = ListUserUseCase(UserRepository(db_session))

    sessions = uc.run()

    db_session.query.assert_called_with(User)
    db_session.query(User).all.assert_called()
    assert len(sessions) == 3
