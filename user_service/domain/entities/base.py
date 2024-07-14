import copy
import uuid

from dataclasses import dataclass, field
from datetime import datetime

from user_service.domain.events.base import BaseEvent


@dataclass(frozen=True)
class BaseEntity:
    """
    Base entity class with common attributes.

    Attributes:
        id (str): Unique identifier for the entity.
        created_at (datetime): Timestamp when the entity was created.
        updated_at (datetime): Timestamp when the entity was last updated.
    """

    oid: str = field(
        default_factory=lambda: str(uuid.uuid4()),
        kw_only=True,
    )
    _events: list[BaseEvent] = field(
        default_factory=list,
        kw_only=True,
    )
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: "BaseEntity") -> bool:
        return self.oid == __value.oid

    def register_event(self, event: BaseEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> list[BaseEvent]:
        registered_events = copy(self._events)
        self._events.clear()

        return registered_events
