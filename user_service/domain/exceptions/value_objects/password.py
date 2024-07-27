from dataclasses import dataclass

from user_service.domain.exceptions.base import DomainException


@dataclass(eq=False)
class InvalidPasswordException(DomainException):
    @property
    def message(self):
        return "Invalid password"


@dataclass(eq=False)
class EmptyPasswordException(DomainException):
    @property
    def message(self):
        return "Password cannot be empty"
