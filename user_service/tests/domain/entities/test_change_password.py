from user_service.domain.entities.user import User
from user_service.domain.events.user import UserUpdatedEvent
from user_service.domain.value_objects.email import Email
from user_service.domain.value_objects.password import Password
from user_service.domain.value_objects.username import Username


def test_change_password(
    user_data: dict[str, Username | Email | Password], new_password: Password
) -> None:
    user = User.create(**user_data)

    updated_user = user.change_password(new_password=new_password)

    # Verify the password is updated
    assert updated_user.username == user_data["username"]
    assert updated_user.email == user_data["email"]
    assert updated_user.password == new_password
    assert isinstance(updated_user, User)

    # Pull events and check
    events: list[UserUpdatedEvent] = updated_user.pull_events()
    assert len(events) == 1
    event = events[0]
    assert isinstance(event, UserUpdatedEvent)

    assert event.user_id == str(user.oid)
    assert event.username == str(user_data["username"])
    assert event.email == str(user_data["email"])
