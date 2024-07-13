from dataclasses import dataclass

from user_service.domain.exceptions.base import DomainException


@dataclass(eq=False)
class InvalidAddressException(DomainException):
    value: str

    @property
    def message(self):
        return f"Invalid address format: {self.value}"


@dataclass(eq=False)
class InvalidZipCodeException(DomainException):
    value: str

    @property
    def message(self):
        return f"Invalid zip code format: {self.value}"
