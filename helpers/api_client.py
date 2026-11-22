import requests
from typing import Any, Final

BASE_URL: Final = "https://jsonplaceholder.typicode.com"


class ApiClient:
    def __init__(self):
        self._session: Final = requests.Session()

    def get(self, path: str) -> requests.Response:
        return self._session.get(f"{BASE_URL}{path}")

    def get_json(self, path: str) -> Any:
        response = self.get(path)
        assert response.status_code == 200

        body = response.json()
        return body

    def finalize(self) -> None:
        self._session.close()
