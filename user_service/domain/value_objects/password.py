import re

from dataclasses import dataclass

from user_service.domain.exceptions.value_objects.password import (
    EmptyPasswordException,
    InvalidPasswordException,
)
from user_service.domain.value_objects.base import BaseValueObject


@dataclass(frozen=True)
class Password(BaseValueObject):
    """
    Value object representing a user's password.

    Attributes:
        value (str): The password string.
    """

    value: str

    def _validate(self) -> None:
        """
        Validate the password.

        Args:
            value (str): The password string to validate.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        if not self.value:
            raise EmptyPasswordException()

        if not (
            len(self.value) >= 8
            and re.search(r"[a-z]", self.value)
            and re.search(r"\d", self.value)
        ):
            raise InvalidPasswordException()
