import unittest
from unittest.mock import Mock, patch

from app.clover_service import access_token_expired, refresh_oauth_tokens


class OAuthTokenTests(unittest.TestCase):
    def test_access_token_expiration(self):
        # fix the current time so both checks are predictable
        with patch("app.clover_service.time.time", return_value=100):
            self.assertTrue(
                access_token_expired({"access_token_expiration": 50})
            )
            self.assertFalse(
                access_token_expired({"access_token_expiration": 150})
            )

    def test_refresh_returns_new_token_pair(self):
        # simulate clover returning replacement tokens
        response = Mock()
        response.json.return_value = {
            "access_token": "new_access_token",
            "refresh_token": "new_refresh_token",
        }

        # replace the real clover request
        with patch("app.clover_service.requests.post", return_value=response) as post:
            result = refresh_oauth_tokens("old_refresh_token")

        self.assertEqual(
            post.call_args.kwargs["json"]["refresh_token"],
            "old_refresh_token",
        )
        self.assertEqual(result["access_token"], "new_access_token")
        self.assertEqual(result["refresh_token"], "new_refresh_token")


if __name__ == "__main__":
    unittest.main()
