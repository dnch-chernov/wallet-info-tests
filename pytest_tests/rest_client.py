"""
HTTP client for api testing.
"""

import logging
import requests

LOGGER = logging.getLogger(__name__)


class Client:
    """
    API client.
    """

    def __init__(self, url: str, timeout: int = 2):
        self.url = url
        self.timeout = timeout
        self.response = None

    def get(self, uri: str, headers: dict = None, params: dict = None):
        """
        Send GET request.
        """
        self.response = requests.get(
            url=self.url + uri, params=params, timeout=self.timeout, headers=headers
        )
        LOGGER.debug(
            "Making GET request to %s with params: %s. Response status code: %d, response body: %s, elapsed time: %s",
            self.url + uri,
            params,
            self.response.status_code,
            self.response.json(),
            self.response.elapsed.total_seconds(),
        )
        return self.response.json()

    def post(self, uri: str, headers: dict = None, payload: dict = None):
        """
        Make POST request.
        """
        self.response = requests.post(
            url=self.url + uri, json=payload, timeout=self.timeout, headers=headers
        )
        LOGGER.debug(
            "Making POST request to %s, payload: %s. Response status code: %d, body: %s",
            self.url + uri,
            payload,
            self.response.status_code,
            self.response.json(),
        )
        return self.response.json()

    def verify(self, json: dict = None, status_code: int = 200):
        """
        Response verification.
        """
        assert (
            self.response.status_code == status_code
        ), f"Incorect status code: expected {status_code}, received {self.response.status_code}"
        if json:
            assert (
                self.response.json() == json
            ), f"Incorrect response: expected {json}, received: {self.response.json()}"
