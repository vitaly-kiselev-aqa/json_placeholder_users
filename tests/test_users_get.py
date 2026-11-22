import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize(
    "user_id, user_name",
    [(5, "Kamren"), (7, "Elwyn.Skiles")],
)
def test_get_single_user(user_id, user_name):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200

    body = response.json()
    assert body["id"] == user_id
    assert body["username"] == user_name


def test_get_user_list():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

    body = response.json()
    assert len(body) == 10
