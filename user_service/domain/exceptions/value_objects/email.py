from dataclasses import dataclass

from user_service.domain.exceptions.base import DomainException


@dataclass(eq=False)
class InvalidEmailException(DomainException):
    text: str

    @property
    def message(self):
        return f"Invalid email address: {self.text}"
