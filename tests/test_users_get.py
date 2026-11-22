import pytest
from typing import Final

EXPECTED_USER_COUNT: Final = 10


@pytest.mark.parametrize(
    "user_id, user_name",
    [(5, "Kamren"), (7, "Elwyn.Skiles")],
)
def test_get_single_user(api_client, user_id, user_name):
    body = api_client.get_json(f"/users/{user_id}")

    assert body["id"] == user_id
    assert body["username"] == user_name


def test_get_user_list(api_client):
    body = api_client.get_json("/users")

    assert len(body) == EXPECTED_USER_COUNT
