import unittest
from unittest.mock import patch

from app.clover_service import access_token_expired


class TokenExpirationTests(unittest.TestCase):
    def test_expired_access_token(self):
        # Fix the current Unix time so the result is predictable.
        with patch("app.clover_service.time.time", return_value=200):
            # An expiration before the current time must be treated as expired.
            result = access_token_expired({"access_token_expiration": 100})

        self.assertTrue(result)

    def test_valid_access_token(self):
        # Fix the current Unix time so the result is predictable.
        with patch("app.clover_service.time.time", return_value=100):
            # An expiration after the current time must remain valid.
            result = access_token_expired({"access_token_expiration": 200})

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
