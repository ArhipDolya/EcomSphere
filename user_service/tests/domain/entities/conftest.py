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


@pytest.fixture
def new_username():
    return Username("Arhip")


@pytest.fixture
def new_email():
    return Email("arhip@example.com")


@pytest.fixture
def new_password():
    return Password("arhip12344321")
