import pytest

from user_service.domain.entities.user import User
from user_service.domain.events.user import UserUpdatedEvent

from user_service.domain.value_objects.email import Email
from user_service.domain.value_objects.password import Password
from user_service.domain.value_objects.username import Username

from user_service.domain.exceptions.value_objects.email import (
    EmptyEmailException,
    InvalidEmailException,
)


def test_change_email(
    user_data: dict[str, Username | Email | Password], new_email: Email
) -> None:
    user = User.create(**user_data)

    updated_user = user.change_email(new_email=new_email)

    # Verify the email is updated
    assert updated_user.username == user_data["username"]
    assert updated_user.email == new_email
    assert updated_user.password == user_data["password"]
    assert isinstance(updated_user, User)

    # Pull events and check
    events: list[UserUpdatedEvent] = updated_user.pull_events()
    assert len(events) == 1
    event = events[0]
    assert isinstance(event, UserUpdatedEvent)

    assert event.user_id == str(user.oid)
    assert event.username == str(user_data["username"])
    assert event.email == str(new_email)


def test_change_email_invalid_format(
    user_data: dict[str, Username | Email | Password]
) -> None:
    user = User.create(**user_data)

    with pytest.raises(InvalidEmailException):
        invalid_email = Email("invalid-email-format")
        user.change_email(new_email=invalid_email)


def test_change_email_empty_string(
    user_data: dict[str, Username | Email | Password]
) -> None:
    user = User.create(**user_data)

    with pytest.raises(EmptyEmailException):
        invalid_email = Email("")
        user.change_email(new_email=invalid_email)


def test_change_email_none(user_data: dict[str, Username | Email | Password]) -> None:
    user = User.create(**user_data)

    with pytest.raises(EmptyEmailException):
        invalid_email = Email(None)
        user.change_email(new_email=invalid_email)
