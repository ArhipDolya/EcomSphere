import re

from dataclasses import dataclass

from user_service.domain.exceptions.value_objects.password import (
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

    def __post_init__(self):
        """
        Post-initialization method to validate the password.

        This method is automatically called after the dataclass's
        __init__ method. It ensures that the password meets the
        specified validation criteria.
        """
        if not self._validate(self.value):
            raise InvalidPasswordException(self.value)

    def _validate(self, value: str) -> bool:
        """
        Validate the password.

        Args:
            value (str): The password string to validate.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        return (
            len(value) >= 8
            and re.search(r"[A-Z]", value)
            and re.search(r"[a-z]", value)
            and re.search(r"\d", value)
        )
