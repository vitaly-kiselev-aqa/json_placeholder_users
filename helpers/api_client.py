import requests

USERS_ENDPOINT = "https://jsonplaceholder.typicode.com"


class ApiClient:
    def __init__(self):
        self._session = requests.Session()

    def get(self, path: str) -> requests.Response:
        return self._session.get(f"{USERS_ENDPOINT}{path}")

    def finalize(self):
        self._session.close()
