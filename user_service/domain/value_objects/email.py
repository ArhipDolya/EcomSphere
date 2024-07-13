import re

from dataclasses import dataclass

from user_service.domain.exceptions.value_objects.email import InvalidEmailException
from user_service.domain.value_objects.base import BaseValueObject


@dataclass(frozen=True)
class Email(BaseValueObject):
    """
    Value object representing a user's email.

    Attributes:
        value (str): The email address string.
    """

    value: str

    def _validate(self) -> None:
        """
        Validate the email address.

        Args:
            value (str): The email address string to validate.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.value):
            raise InvalidEmailException(self.value)

    def __str__(self) -> str:
        return self.value
