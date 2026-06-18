import unittest
from unittest.mock import patch

import requests

from app.clover_service import get_headers


class OAuthTokenTests(unittest.TestCase):
    def test_expired_token_is_refreshed_and_stored(self):
        # simulate an expired stored token and its replacement
        stored_tokens = {
            "access_token": "old_access_token",
            "access_token_expiration": 50,
            "refresh_token": "old_refresh_token",
            "merchant_id": "merchant_id",
        }
        new_tokens = {
            "access_token": "new_access_token",
            "access_token_expiration": 150,
            "refresh_token": "new_refresh_token",
        }

        with (
            patch("app.clover_service.time.time", return_value=100),
            patch("app.clover_service.load_oauth_tokens", return_value=stored_tokens),
            patch("app.clover_service.refresh_oauth_tokens", return_value=new_tokens),
            patch("builtins.open"),
            patch("app.clover_service.json.dump") as dump,
            patch("app.clover_service.os.chmod"),
        ):
            headers = get_headers()

        self.assertEqual(headers["Authorization"], "Bearer new_access_token")
        self.assertEqual(dump.call_args.args[0]["merchant_id"], "merchant_id")

    def test_failed_refresh_requires_authorization(self):
        # return a clear reconnect message when clover rejects the refresh
        stored_tokens = {
            "access_token_expiration": 50,
            "refresh_token": "old_refresh_token",
        }

        with (
            patch("app.clover_service.time.time", return_value=100),
            patch("app.clover_service.load_oauth_tokens", return_value=stored_tokens),
            patch(
                "app.clover_service.refresh_oauth_tokens",
                side_effect=requests.HTTPError(),
            ),
            self.assertRaisesRegex(RuntimeError, "/oauth/start"),
        ):
            get_headers()


if __name__ == "__main__":
    unittest.main()
