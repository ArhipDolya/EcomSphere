from dataclasses import dataclass

from user_service.domain.exceptions.base import DomainException


@dataclass(eq=False)
class InvalidPasswordException(DomainException):
    @property
    def message(self):
        return "Invalid password"
