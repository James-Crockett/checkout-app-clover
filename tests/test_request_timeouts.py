import unittest
from unittest.mock import Mock, patch

from app.clover_service import (
    add_line_item,
    create_card_token,
    create_order,
    pay_order,
)
from app.main import oauth_callback


class RequestTimeoutTests(unittest.TestCase):
    def test_create_order_uses_timeout(self):
        # Return a successful fake response so no Clover request is made.
        response = Mock()
        response.json.return_value = {"id": "order_id"}

        # Confirm create_order limits how long it waits for Clover.
        with (
            patch("app.clover_service.requests.post", return_value=response) as post,
            patch(
                "app.clover_service.load_oauth_tokens",
                return_value={"access_token": "test_token"},
            ),
        ):
            create_order()

        self.assertEqual(post.call_args.kwargs["timeout"], 10)

    def test_add_line_item_uses_timeout(self):
        # Return a successful fake response so no Clover request is made.
        response = Mock()
        response.json.return_value = {"id": "line_item_id"}

        # Confirm add_line_item limits how long it waits for Clover.
        with (
            patch("app.clover_service.requests.post", return_value=response) as post,
            patch(
                "app.clover_service.load_oauth_tokens",
                return_value={"access_token": "test_token"},
            ),
        ):
            add_line_item("order_id", "Test item", 100)

        self.assertEqual(post.call_args.kwargs["timeout"], 10)

    def test_pay_order_uses_timeout(self):
        # Return a successful fake response so no Clover request is made.
        response = Mock(status_code=200, text="{}")

        # Confirm pay_order limits how long it waits for Clover.
        with patch("app.clover_service.requests.post", return_value=response) as post:
            pay_order("order_id", "source_token")

        self.assertEqual(post.call_args.kwargs["timeout"], 10)

    def test_create_card_token_uses_timeout(self):
        # Return a successful fake response so no Clover request is made.
        response = Mock()
        response.json.return_value = {"id": "token_id"}

        # Confirm create_card_token limits how long it waits for Clover.
        with patch("app.clover_service.requests.post", return_value=response) as post:
            create_card_token()

        self.assertEqual(post.call_args.kwargs["timeout"], 10)

    def test_oauth_callback_uses_timeout(self):
        # Return a successful fake token response so no Clover request is made.
        response = Mock(status_code=200)
        response.json.return_value = {"access_token": "test_token"}

        # Confirm the OAuth token exchange limits how long it waits for Clover.
        with (
            patch("app.main.requests.post", return_value=response) as post,
            patch("builtins.open"),
            patch("app.main.os.chmod"),
        ):
            oauth_callback("authorization_code")

        self.assertEqual(post.call_args.kwargs["timeout"], 10)


if __name__ == "__main__":
    unittest.main()
