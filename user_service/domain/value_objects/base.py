from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseValueObject(ABC):
    @abstractmethod
    def _validate(self) -> None:
        ...

    def __post_init__(self) -> None:
        self._validate()
