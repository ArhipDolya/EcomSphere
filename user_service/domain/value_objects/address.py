import re

from dataclasses import dataclass

from user_service.domain.exceptions.value_objects.address import (
    InvalidAddressException,
    InvalidZipCodeException,
)

from user_service.domain.value_objects.base import BaseValueObject


@dataclass(frozen=True)
class Address(BaseValueObject):
    country: str
    street: str
    city: str
    zip_code: str

    def _validate(self) -> None:
        if not all([self.country, self.street, self.city, self.zip_code]):
            raise InvalidAddressException("All address fields must be provided")

        if len(self.street) < 3:
            raise InvalidAddressException("Street must be at least 3 characters long")

        if len(self.city) < 2:
            raise InvalidAddressException("City must be at least 2 characters long")

        self._validate_zip_code()

    def _validate_zip_code(self):
        if not re.match(r"^\d{5}(-\d{4})?$", self.zip_code):
            raise InvalidZipCodeException(f"Invalid zip code format: {self.zip_code}")

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.zip_code}, {self.country}"
