"""
API tests
"""

import pytest

class TestStatus:
    """
    Tests for /api/status endpoint.
    """

    def test_status(self, client):
        """
        Happy path test.
        """
        client.get("/api/status")
        print(f"\n ~~> time: {client.response.elapsed.total_seconds()}")
        client.verify(json={"status":"Still alive!"})

class TestBalance:
    """
    Tests for /api/balance endpoint.
    """

    @pytest.mark.parametrize("token, value", [
        ("eth", 0.024925767330357063),
        ("usdc", 61.280028)
    ])
    def test_balance_eth_positive(self, client, token, value):
        """
        Happy path tests for /api/balance endpoint.
        """
        client.get(f"/api/balance/{token}/0x300045c41b5334772C25196ac0035bCDD511a821")
        client.verify(json={"crypto": token, "balance": value})
