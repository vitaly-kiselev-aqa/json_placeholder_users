import pytest

from schemas.user import User
from tests.expected_user_count import EXPECTED_USER_COUNT


@pytest.mark.parametrize(
    ("user_id", "user_name"),
    [(5, "Kamren"), (7, "Elwyn.Skiles")],
)
def test_get_single_user(api, user_id, user_name):
    user = api.get(f"/users/{user_id}", User)

    assert user.id == user_id
    assert user.username == user_name


def test_get_user_list(api):
    users = api.get("/users", list[User])

    assert len(users) == EXPECTED_USER_COUNT
