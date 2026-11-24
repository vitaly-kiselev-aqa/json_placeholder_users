from http import HTTPStatus
from typing import Any, Final

import requests

BASE_URL: Final = "https://jsonplaceholder.typicode.com"


class ApiClient:
    def __init__(self):
        self._session: Final = requests.Session()

    @staticmethod
    def _make_url(path: str) -> str:
        return f"{BASE_URL}{path}"

    def get(self, path: str) -> requests.Response:
        url = self._make_url(path)
        return self._session.get(url)

    def get_json(self, path: str) -> Any:
        response = self.get(path)
        assert response.status_code == HTTPStatus.OK

        body = response.json()
        return body

    def post_json(self, path: str, body: dict[str, Any]) -> Any:
        url = self._make_url(path)

        response = self._session.post(url, json=body)
        assert response.status_code == HTTPStatus.CREATED

        body = response.json()
        return body

    def finalize(self) -> None:
        self._session.close()
