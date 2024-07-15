from user_service.domain.entities.user import User
from user_service.domain.events.user import UserCreatedEvent
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
