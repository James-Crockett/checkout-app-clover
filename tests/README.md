# Tests

## `test_clover_service.py`

Tests Clover service behavior without making real network requests.

The current test simulates Clover rejecting a payment and verifies that
`pay_order()` raises an HTTP error instead of treating the payment as successful.

## `test_oauth_storage.py`

Verifies that the OAuth callback stores the access token, refresh token, and
merchant ID locally with owner-only file permissions.

## `test_oauth_tokens.py`

Verifies that expired tokens are refreshed and stored, and that failed refreshes
require OAuth authorization again.
