import pytest

from user_service.domain.events.user import UserCreatedEvent


def test_user_created_event_with_valid_data(user_data):
    """Test that UserCreatedEvent has correct attributes."""
    event = UserCreatedEvent(**user_data)

    assert event.user_id == user_data["user_id"]
    assert event.username == user_data["username"]
    assert event.email == user_data["email"]
    assert isinstance(event, UserCreatedEvent)


def test_user_created_event_with_missing_fields():
    incomplete_data = {
        "user_id": "123e4567-e89b-12d3-a456-426614174000",
        "username": "john_doe",
    }
    with pytest.raises(TypeError) as excinfo:
        UserCreatedEvent(**incomplete_data)
    assert "missing 1 required positional argument: 'email'" in str(excinfo.value)
