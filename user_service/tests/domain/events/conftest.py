import pytest


@pytest.fixture
def user_data():
    """Fixture for user data."""
    return {
        "user_id": "123e4567-e89b-12d3-a456-426614174000",
        "username": "john_doe",
        "email": "john@example.com",
    }


@pytest.fixture
def updated_user_data():
    """Fixture for updated user data."""
    return {
        "user_id": "123e4567-e89b-12d3-a456-426614174000",
        "username": "john_doe_updated",
        "email": "john_updated@example.com",
    }
