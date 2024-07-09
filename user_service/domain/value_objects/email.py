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

    def __post_init__(self):
        """
        Post-initialization method to validate the email.

        This method is automatically called after the dataclass's
        __init__ method. It ensures that the email meets the
        specified validation criteria.
        """
        if not self._validate(self.value):
            raise InvalidEmailException(self.value)

    def _validate(self, value: str) -> bool:
        """
        Validate the email address.

        Args:
            value (str): The email address string to validate.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", value))
