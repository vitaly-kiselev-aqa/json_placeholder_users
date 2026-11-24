from expected_user_count import EXPECTED_USER_COUNT
from schemas.created_user import CreatedUser


def test_create_user(api):
    new_user_name = "John"
    new_user = {"name": new_user_name}

    created_user = api.post("/users", new_user, CreatedUser)

    new_user_id = EXPECTED_USER_COUNT + 1

    assert created_user.id == new_user_id
    assert created_user.name == new_user_name
