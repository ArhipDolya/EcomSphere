from abc import ABC
from dataclasses import dataclass


@dataclass(eq=False)
class DomainException(ABC):
    @property
    def message(self):
        return "There was domain error"
