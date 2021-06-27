"""Test Session use case."""
from unittest.mock import MagicMock
from unittest.mock import Mock

from app.session.models.repository import SessionRepository
from app.session.models.session import Session
from app.session.usecase.create_session import CreateSessionUseCase
from app.session.usecase.list_session import ListSessionUseCase
from app.user.models.repository import UserRepository
from app.user.models.user import User


def test_use_case_create_session():
    """Test create session."""
    db_session = MagicMock()
    user = MagicMock()

    db_session.query(User).return_value.filter_by.return_value.one.return_value = user

    uc = CreateSessionUseCase(SessionRepository(db_session), UserRepository(db_session))

    uc.run(1, '09:15')

    db_session.query.assert_called_with(User)
    db_session.query(User).filter_by(id=1).one.assert_called()
    db_session.add.assert_called()


def test_use_case_list_session():
    """Teste list session."""
    db_session = MagicMock()
    session_list = [Mock(), Mock(), Mock()]
    db_session.query(Session).all.return_value = session_list

    uc = ListSessionUseCase(SessionRepository(db_session))

    sessions = uc.run()

    db_session.query.assert_called_with(Session)
    db_session.query(Session).all.assert_called()
    assert len(sessions) == 3
