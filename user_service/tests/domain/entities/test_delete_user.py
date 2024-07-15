from user_service.domain.entities.user import User
from user_service.domain.events.user import UserDeletedEvent
from user_service.domain.value_objects.email import Email
from user_service.domain.value_objects.password import Password
from user_service.domain.value_objects.username import Username


def test_delete_user(user_data: dict[str, Username | Email | Password]) -> None:
    user = User.create(**user_data)

    user.pull_events()

    user.delete()

    # Pull events and check
    events: list[UserDeletedEvent] = user.pull_events()
    assert len(events) == 1
    event = events[0]
    assert isinstance(event, UserDeletedEvent)
    assert event.user_id == str(user.oid)
    assert event.username == str(user_data["username"])
    assert event.email == str(user_data["email"])
