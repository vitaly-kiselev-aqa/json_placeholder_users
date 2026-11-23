from expected_user_count import EXPECTED_USER_COUNT


def test_create_user(api_client):
    new_user_name = "John"
    new_user = {"name": new_user_name}

    created_user = api_client.post_json("/users", new_user)

    new_user_id = EXPECTED_USER_COUNT + 1

    assert created_user["id"] == new_user_id
    assert created_user["name"] == new_user_name
