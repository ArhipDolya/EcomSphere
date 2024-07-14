from user_service.domain.entities.user import User
from user_service.domain.events.user import UserCreatedEvent


def test_user_creation(user_data):
    user = User.create(**user_data)

    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
    assert user.password == user_data["password"]
    assert isinstance(user, User)

    # Check if the UserCreatedEvent is registered
    assert len(user._events) == 1
    event = user._events[0]
    assert isinstance(event, UserCreatedEvent)

    assert event.user_id == str(user.oid)
    assert event.username == str(user_data["username"])
    assert event.email == str(user_data["email"])
