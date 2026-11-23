import pytest
from expected_user_count import EXPECTED_USER_COUNT


@pytest.mark.parametrize(
    "user_id, user_name",
    [(5, "Kamren"), (7, "Elwyn.Skiles")],
)
def test_get_single_user(api_client, user_id, user_name):
    user = api_client.get_json(f"/users/{user_id}")

    assert user["id"] == user_id
    assert user["username"] == user_name


def test_get_user_list(api_client):
    users = api_client.get_json("/users")

    assert len(users) == EXPECTED_USER_COUNT
