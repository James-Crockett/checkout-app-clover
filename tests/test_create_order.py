import unittest
from unittest.mock import Mock, patch

from app.clover_service import create_order


class CreateOrderTests(unittest.TestCase):
    def test_create_order_uses_timeout(self):
        # Return a successful fake response so no Clover request is made.
        response = Mock()
        response.json.return_value = {"id": "order_id"}

        # Confirm create_order limits how long it waits for Clover.
        with patch("app.clover_service.requests.post", return_value=response) as post:
            create_order()

        self.assertEqual(post.call_args.kwargs["timeout"], 10)


if __name__ == "__main__":
    unittest.main()
