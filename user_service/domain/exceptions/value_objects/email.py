from dataclasses import dataclass

from user_service.domain.exceptions.base import DomainException


@dataclass(eq=False)
class InvalidEmailException(DomainException):
    value: str

    @property
    def message(self):
        return f"Invalid email address: {self.value}"


@dataclass(eq=False)
class EmptyEmailException(DomainException):
    @property
    def message(self):
        return "Email cannot be empty"
