from dataclasses import dataclass

from user_service.domain.value_objects.base import BaseValueObject


@dataclass(frozen=True)
class Address(BaseValueObject):
    country: str
    street: str
    city: str
    zip_code: str
