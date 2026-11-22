import pytest

from helpers.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client():
    client = ApiClient()
    yield client
    client.finalize()
