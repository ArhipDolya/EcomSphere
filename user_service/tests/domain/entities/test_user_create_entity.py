import pytest

from user_service.domain.entities.user import User
from user_service.domain.events.user import UserCreatedEvent
from user_service.domain.exceptions.value_objects.email import InvalidEmailException
from user_service.domain.exceptions.value_objects.password import (
    InvalidPasswordException,
)
from user_service.domain.exceptions.value_objects.username import (
    EmptyUsernameException,
)
from user_service.domain.value_objects.username import Username
from user_service.domain.value_objects.email import Email
from user_service.domain.value_objects.password import Password


def test_user_creation(user_data: dict[str, Username | Email | Password]) -> None:
    user = User.create(**user_data)

    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
    assert user.password == user_data["password"]
    assert isinstance(user, User)

    # Check if the UserCreatedEvent is registered
    events: list[UserCreatedEvent] = user.pull_events()
    assert len(events) == 1
    event = events[0]
    assert isinstance(event, UserCreatedEvent)

    assert event.user_id == str(user.oid)
    assert event.username == str(user_data["username"])
    assert event.email == str(user_data["email"])


def test_user_creation_invalid_email(
    user_data: dict[str, Username | Email | Password]
) -> None:
    with pytest.raises(InvalidEmailException):
        user_data["email"] = Email("invalid-email")
        User.create(**user_data)


def test_user_creation_invalid_password(
    user_data: dict[str, Username | Email | Password]
) -> None:
    with pytest.raises(InvalidPasswordException):
        user_data["password"] = Password("short")
        User.create(**user_data)


def test_user_creation_invalid_username(
    user_data: dict[str, Username | Email | Password]
) -> None:
    with pytest.raises(EmptyUsernameException):
        user_data["username"] = Username("")
        User.create(**user_data)
