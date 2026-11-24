import pytest

from helpers.api import Api


@pytest.fixture(scope="session")
def api():
    api = Api()
    yield api
    api.finalize
