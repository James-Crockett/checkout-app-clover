# checkout-app-clover

A local checkout prototype that creates and pays Clover sandbox orders

## Setup

Requires Python 3.12, `uv`, a Clover sandbox app, and a test merchant

```bash
uv sync
cp .env.example .env
```

Fill `.env` with Clover sandbox URLs, app credentials, redirect URI, and Ecommerce tokens

## Run

```bash
uv run uvicorn app.main:app --reload
python -m http.server 5500 --directory frontend
```

Run each command in a separate terminal and open `http://localhost:5500`

## OAuth

1. Open `http://localhost:8000/oauth/start` and authorize the app
2. Clover redirects to `/oauth/callback`
3. The backend stores the token pair and merchant ID
4. Merchant requests use the stored token and refresh it once when expired
5. A failed refresh requires authorization through `/oauth/start` again

Tokens are stored in Git-ignored `app/oauth_tokens.json` with owner-only permissions

## Payment Flow

The frontend sends amount and description to `POST /api/payments`

- create an order with `POST /v3/merchants/{merchant_id}/orders`
- add a line item with `POST /orders/{order_id}/line_items`
- create a sandbox card token with `POST /v1/tokens`
- pay the order with `POST /v1/orders/{order_id}/pay`

The response displays payment status and appends it to `app/transaction.log`

## Tests

Run `python -m unittest discover -s tests -v` See `tests/README.md` for details
