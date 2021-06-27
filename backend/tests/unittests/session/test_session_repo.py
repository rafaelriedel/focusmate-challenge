"""Test Session repository."""
from unittest.mock import MagicMock, Mock
import pytest

from app.session.models.repository import SessionRepository


def test_session_add():
    """Test add session."""
    session = Mock()
    session = MagicMock()
    repo = SessionRepository(session)
    repo.add(session)

    session.add.assert_called_with(session)


def test_session_get_by_id_should_find():
    """Test session get_by_id: it should find."""
    session = Mock()
    session = MagicMock()

    session.query.return_value.filter_by.return_value.one.return_value = session

    repo = SessionRepository(session)

    assert session == repo.get_by_id(1)


def test_session_get_by_id_should_not_find():
    """Test session get_by_id: it should not find."""
    session = Mock()
    session = MagicMock()

    session.query.return_value.filter_by.return_value.one.side_effect = Exception()

    with pytest.raises(Exception):
        repo = SessionRepository(session)
        repo.get_by_id(1)


def test_session_list():
    """Test session list."""
    session = MagicMock()

    session.query.return_value.all.return_value = [Mock(), Mock()]

    repo = SessionRepository(session)
    assert len(repo.list()) == 2
