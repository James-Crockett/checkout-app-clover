## Initial setup

Added uv for installing dependencies
Added .gitignore

Added the following libs:
fastapi - API framework
uvicorn - for interacting with sockets
requests - for making HTTP requests
python-dotenv - for loading secret tolkens from .env file

## Rough Structure

Before I go into building the application, I forgot to go into the structure of the assignment/breaking it down.

## Objective of the assignment

A web based checkout app integrated with a clover api

## Input

By the requirements, the user has to give:
- An amount - int
- Product name - char
- A trigger after entering or submit action

## Inupt from backend

Clover would have config values, at this stage not sure what values id be using, have to refer the docs

## Backend

After the submission, the backend should:
- Validate the amount
- Convert to cents since this is a starndard, not complicating with money var
- Create clover order
- Added line item to order
- Initiate payment
- Fetch the payment status
- Log the transaction
- Return the status to the front end

## Clover Integration

- Create clover config
- Create clover acc
- Create env.example file
- Add Clover deps
- Create clover service
- Write it to /api/payments

## Things I noticed after a initial project completion

- Fix failed payment handling

> when looking at the transaction logs, i saw some transactions failed because the card was used too much and clover recognized it but it gave 200 anyways. this should have been flaged as a failed transaction, it even shows up in the clover portal.

/home/james_crockett/Projects/checkout-app-clover/failed_transactions.png

- Money conversion

> it is using the int var, im not sure it would be a good choice, have to reasearch.

- OAuth is incomplete

> after looking at the document, i realized the token handling is incomplete.

- work on documentation and comments

> have to work on documentation and update comments throughout the repo.

- Error handling

> have to work more on edge cases and error handling, like the first issue.

- Cleanup

> go though the repo and cleanup some stuff.
