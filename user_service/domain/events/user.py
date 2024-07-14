from dataclasses import dataclass

from user_service.domain.events.base import BaseEvent


@dataclass(frozen=True)
class UserCreatedEvent(BaseEvent):
    user_id: str
    username: str
    email: str


@dataclass(frozen=True)
class UserUpdatedEvent(BaseEvent):
    user_id: str
    username: str
    email: str


@dataclass(frozen=True)
class UserDeletedEvent(BaseEvent):
    user_id: str
    username: str
    email: str
