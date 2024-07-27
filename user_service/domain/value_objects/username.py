import re

from dataclasses import dataclass

from user_service.domain.exceptions.value_objects.username import (
    EmptyUsernameException,
    InvalidUsernameException,
    TooLongUsernameException,
)

from user_service.domain.value_objects.base import BaseValueObject


MAX_USERNAME_LENGTH = 22
USERNAME_PATTERN = re.compile(r"^[a-zA-Z0-9_]+$")


@dataclass(frozen=True)
class Username(BaseValueObject):
    value: str | None

    def _validate(self) -> None:
        if not self.value:
            raise EmptyUsernameException(self.value)
        if len(self.value) > MAX_USERNAME_LENGTH:
            raise TooLongUsernameException(self.value)
        if not USERNAME_PATTERN.match(self.value):
            raise InvalidUsernameException(self.value)

    def __str__(self) -> str:
        return str(self.value) if self.value is not None else ""

    def exists(self) -> bool:
        return self.value is not None
