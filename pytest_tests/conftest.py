"""
conftest.py
"""
import os
import pytest
from rest_client import Client


@pytest.fixture(scope="session")
def client():
    """
    API test client fixture.
    """
    yield Client(url=os.getenv("BACKEND_URL"))
