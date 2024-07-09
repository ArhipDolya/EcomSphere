from dataclasses import dataclass, field
from datetime import datetime

from user_service.domain.entities.base import BaseEntity
from user_service.domain.events.user import UserDeletedEvent, UserUpdatedEvent

from user_service.domain.value_objects.address import Address
from user_service.domain.value_objects.password import Password
from user_service.domain.value_objects.email import Email


@dataclass(frozen=True)
class User(BaseEntity):
    """
    Entity representing a user in the system.

    Attributes:
        name (str): The user's name.
        email (Email): The user's email address.
        password (Password): The user's password.
        addresses (list[Address]): A list of the user's addresses.
    """

    name: str
    email: Email
    password: Password
    addresses: list[Address] = field(default_factory=list)

    def change_email(self, new_email: Email) -> "User":
        """
        Change the user's email address.

        Args:
            new_email (Email): The new email address.
        """
        updated_user = User(
            id=self.id,
            name=self.name,
            email=new_email,
            password=self.password,
            addresses=self.addresses,
            created_at=self.created_at,
            updated_at=datetime.now(),
        )
        updated_user.register_event(
            UserUpdatedEvent(user_id=self.id, name=self.name, email=str(new_email))
        )
        return updated_user

    def change_password(self, new_password: Password) -> "User":
        """
        Change the user's password.

        Args:
            new_password (Password): The new password.
        """
        updated_user = User(
            id=self.id,
            name=self.name,
            email=self.email,
            password=new_password,
            addresses=self.addresses,
            created_at=self.created_at,
            updated_at=datetime.now(),
        )
        updated_user.register_event(
            UserUpdatedEvent(user_id=self.id, name=self.name, email=str(self.email))
        )
        return updated_user

    def delete(self) -> None:
        self.register_event(
            UserDeletedEvent(user_id=self.id, name=self.name, email=str(self.email))
        )
