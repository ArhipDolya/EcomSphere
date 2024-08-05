from dataclasses import dataclass

from user_service.domain.exceptions.base import DomainException


@dataclass(eq=False)
class InvalidRoleException(DomainException):
    role: str

    @property
    def message(self) -> str:
        return f"Invalid role: {self.role}"


@dataclass(eq=False)
class EmptyRoleException(DomainException):
    @property
    def message(self) -> str:
        return "Role cannot be empty"
