import pytest

from app import app

@pytest.fixture(scope="module")
def user_app():
    return app