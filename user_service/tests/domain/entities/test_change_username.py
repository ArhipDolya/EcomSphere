import pytest

from user_service.domain.entities.user import User
from user_service.domain.events.user import UserUpdatedEvent
from user_service.domain.exceptions.value_objects.username import (
    EmptyUsernameException,
    TooLongUsernameException,
)
from user_service.domain.value_objects.email import Email
from user_service.domain.value_objects.password import Password
from user_service.domain.value_objects.username import Username


def test_change_username(
    user_data: dict[str, Username | Email | Password], new_username: Username
) -> None:
    user = User.create(**user_data)

    # Change username
    updated_user = user.change_username(new_username=new_username)

    # Verify the username is updated
    assert updated_user.username == new_username
    assert updated_user.email == user_data["email"]
    assert updated_user.password == user_data["password"]
    assert isinstance(updated_user, User)

    # Pull events and check
    events: list[UserUpdatedEvent] = updated_user.pull_events()
    assert len(events) == 1
    event = events[0]
    assert isinstance(event, UserUpdatedEvent)

    assert event.user_id == str(user.oid)
    assert event.username == str(new_username)
    assert event.email == str(user_data["email"])


def test_change_username_empty_string(
    user_data: dict[str, Username | Email | Password], new_username: Username
) -> None:
    user = User.create(**user_data)

    with pytest.raises(EmptyUsernameException):
        new_username = Username("")
        user.change_username(new_username=new_username)


def test_change_username_too_long(
    user_data: dict[str, Username | Email | Password], new_username: Username
) -> None:
    user = User.create(**user_data)

    with pytest.raises(TooLongUsernameException):
        new_username = Username("username" * 23)
        user.change_username(new_username=new_username)
