from user_service.domain.events.user import UserDeletedEvent


def test_user_deleted_event(user_data):
    """Test that UserDeletedEvent has correct attributes."""
    event = UserDeletedEvent(**user_data)

    assert event.user_id == user_data["user_id"]
    assert event.username == user_data["username"]
    assert event.email == user_data["email"]
    assert isinstance(event, UserDeletedEvent)
