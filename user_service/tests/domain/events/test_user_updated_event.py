from user_service.domain.events.user import UserUpdatedEvent


def test_user_updated_event(updated_user_data):
    """Test that UserUpdatedEvent has correct attributes."""
    event = UserUpdatedEvent(**updated_user_data)

    assert event.user_id == updated_user_data["user_id"]
    assert event.username == updated_user_data["username"]
    assert event.email == updated_user_data["email"]
    assert isinstance(event, UserUpdatedEvent)
