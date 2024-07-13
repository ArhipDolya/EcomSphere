from dataclasses import dataclass

from user_service.domain.exceptions.base import DomainException


@dataclass(eq=False)
class InvalidUsernameException(DomainException):
    username: str

    @property
    def message(self) -> str:
        return f"Username is invalid: {self.username}"


@dataclass(eq=False)
class EmptyUsernameException(DomainException):
    username: str

    @property
    def message(self) -> str:
        return f"Username cannot be empty: {self.username}"


@dataclass(eq=False)
class TooLongUsernameException(DomainException):
    username: set

    @property
    def message(self) -> str:
        return f"Username is too long: {self.username}"
