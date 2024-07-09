from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class BaseEvent(ABC):
    event_id: str = field(default_factory=uuid4, kw_only=True)
    created_at: datetime = field(default_factory=datetime.now)
