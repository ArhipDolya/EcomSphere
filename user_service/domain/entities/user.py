from dataclasses import dataclass, field
from datetime import datetime

from user_service.domain.entities.base import BaseEntity
from user_service.domain.events.user import (
    UserCreatedEvent,
    UserDeletedEvent,
    UserRoleAddedEvent,
    UserRoleRemovedEvent,
    UserUpdatedEvent,
)
from user_service.domain.value_objects.address import Address

from user_service.domain.value_objects.password import Password
from user_service.domain.value_objects.email import Email
from user_service.domain.value_objects.username import Username
from user_service.domain.value_objects.role import Role


@dataclass(frozen=True)
class User(BaseEntity):
    username: Username
    email: Email
    password: Password
    is_active: bool = True
    last_login: datetime | None = None
    addresses: list[Address] = field(default_factory=list)
    roles: list[Role] = field(default_factory=list)

    @classmethod
    def create(cls, username: Username, email: Email, password: Password) -> "User":
        new_user = cls(
            username=username,
            email=email,
            password=password,
        )

        new_user.register_event(
            UserCreatedEvent(
                user_id=str(new_user.oid), username=str(username), email=str(email)
            )
        )

        return new_user

    def change_username(self, new_username: Username) -> "User":
        updated_user = User(
            oid=self.oid,
            username=new_username,
            email=self.email,
            password=self.password,
            addresses=self.addresses,
            created_at=self.created_at,
        )
        updated_user.register_event(
            UserUpdatedEvent(
                user_id=str(self.oid), username=str(new_username), email=str(self.email)
            )
        )
        return updated_user

    def change_email(self, new_email: Email) -> "User":
        updated_user = User(
            oid=self.oid,
            username=self.username,
            email=new_email,
            password=self.password,
            addresses=self.addresses,
            created_at=self.created_at,
        )
        updated_user.register_event(
            UserUpdatedEvent(
                user_id=str(self.oid), username=str(self.username), email=str(new_email)
            )
        )
        return updated_user

    def change_password(self, new_password: Password) -> "User":
        updated_user = User(
            oid=self.oid,
            username=self.username,
            email=self.email,
            password=new_password,
            addresses=self.addresses,
            created_at=self.created_at,
        )
        updated_user.register_event(
            UserUpdatedEvent(
                user_id=str(self.oid),
                username=str(self.username),
                email=str(self.email),
            )
        )
        return updated_user

    def delete(self) -> None:
        self.register_event(
            UserDeletedEvent(
                user_id=self.oid, username=str(self.username), email=str(self.email)
            )
        )

    def add_role(self, role: Role) -> "User":
        if role not in self.roles:
            updated_roles = self.roles + [role]
            updated_user = User(
                oid=self.oid,
                username=self.username,
                email=self.email,
                password=self.password,
                addresses=self.addresses,
                is_active=self.is_active,
                last_login=self.last_login,
                roles=updated_roles,
                created_at=self.created_at,
            )

            updated_user.register_event(
                UserRoleAddedEvent(
                    user_id=str(self.oid),
                    username=str(self.username),
                    email=str(self.email),
                    role=str(role),
                )
            )

            return updated_user
        return self

    def remove_role(self, role: Role) -> "User":
        updated_roles = [r for r in self.roles if r != role]
        updated_user = User(
            oid=self.oid,
            username=self.username,
            email=self.email,
            password=self.password,
            addresses=self.addresses,
            is_active=self.is_active,
            last_login=self.last_login,
            roles=updated_roles,
            created_at=self.created_at,
        )

        if updated_roles != self.roles:
            updated_user.register_event(
                UserRoleRemovedEvent(
                    user_id=str(self.oid),
                    username=str(self.username),
                    email=str(self.email),
                    role=str(role),
                )
            )

        return updated_user

    def authenticate(self, password: str) -> bool:
        return self.password.verify(password)
