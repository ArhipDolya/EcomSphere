import pytest

from user_service.domain.value_objects.username import Username
from user_service.domain.value_objects.email import Email
from user_service.domain.value_objects.password import Password


@pytest.fixture
def user_data():
    return {
        "username": Username("john_doe"),
        "email": Email("john@example.com"),
        "password": Password("securepassword123"),
    }
