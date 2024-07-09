from dataclasses import dataclass

from user_service.domain.events.base import BaseEvent


@dataclass
class UserCreatedEvent(BaseEvent):
    user_id: str
    name: str
    email: str


@dataclass
class UserUpdatedEvent(BaseEvent):
    user_id: str
    name: str
    email: str


@dataclass
class UserDeletedEvent(BaseEvent):
    user_id: str
    name: str
    email: str
