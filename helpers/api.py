from pydantic import TypeAdapter
from typing import Any, TypeVar, Final

from .api_client import ApiClient

T = TypeVar("T")


class Api:
    def __init__(self):
        self._client: Final[ApiClient] = ApiClient()

    @staticmethod
    def _parse_response(response: Any, response_type: type[T]) -> T:
        adapter = TypeAdapter(response_type)
        return adapter.validate_python(response)

    def get(self, path: str, response_type: type[T]) -> T:
        response = self._client.get_json(path)
        return self._parse_response(response, response_type)

    def post(self, path: str, body: dict[str, Any], response_type: type[T]) -> T:
        response = self._client.post_json(path, body)
        return self._parse_response(response, response_type)

    def finalize(self) -> None:
        self._client.finalize()
