# Tests

## `test_clover_service.py`

Tests Clover service behavior without making real network requests.

The current test simulates Clover rejecting a payment and verifies that
`pay_order()` raises an HTTP error instead of treating the payment as successful.

## `test_create_order.py`

Verifies that `create_order()` applies a timeout to its Clover request without
contacting the real Clover API.
