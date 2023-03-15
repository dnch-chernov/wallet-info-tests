"""
API tests
"""

import os
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
        client.verify(json={"connected": True})


class TestBalance:
    """
    Tests for /api/balance endpoint.
    """

    wallet_address = os.getenv(
        "WALLET_ADDRESS", "0x300045c41b5334772C25196ac0035bCDD511a821"
    )
    expected_eth_value = os.getenv("EXPECTED_ETH_VALUE", "0.024925767330357063")
    expected_usdc_value = os.getenv("EXPECTED_USDC_VALUE", "61.280028")

    @pytest.mark.parametrize(
        "token, value", [("eth", expected_eth_value), ("usdc", expected_usdc_value)]
    )
    def test_balance_eth_positive(self, client, token, value):
        """
        Happy path tests for /api/balance endpoint.
        """
        client.get(f"/api/balance/{token}/{self.wallet_address}")
        client.verify(json={"crypto": token, "balance": value})
