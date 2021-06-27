"""Test User repository."""
from unittest.mock import MagicMock, Mock
import pytest

from app.user.models.repository import UserRepository


def test_user_add():
    """Test add user."""
    user = Mock()
    session = MagicMock()
    repo = UserRepository(session)
    repo.add(user)

    session.add.assert_called_with(user)


def test_user_get_by_id_should_find():
    """Test user get_by_id: it should find."""
    user = Mock()
    session = MagicMock()

    session.query.return_value.filter_by.return_value.one.return_value = user

    repo = UserRepository(session)

    assert user == repo.get_by_id(1)


def test_user_get_by_id_should_not_find():
    """Test session get_by_id: it should not find."""
    session = MagicMock()

    session.query.return_value.filter_by.return_value.one.side_effect = Exception()

    with pytest.raises(Exception):
        repo = UserRepository(session)
        repo.get_by_id(1)


def test_user_list():
    """Test session list."""
    session = MagicMock()

    session.query.return_value.all.return_value = [Mock(), Mock()]

    repo = UserRepository(session)
    assert len(repo.list()) == 2
