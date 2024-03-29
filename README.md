# Checking out Supermarket Cart

[![Python Version](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://python.org)
[![FastAPI Version](https://img.shields.io/badge/fastapi-0.108-brightgreen.svg)](https://fastapi.tiangolo.com)
-----------------------------------------------------------------------------------------------------------------
An implementation of a supermarket checkout that calculates the total price of purchased items using Fast API.

The APIs are deployed to test the entire functionality https://supermarket-checkout-gautam.koyeb.app/docs


## Case Description
 Implement the code for a supermarket checkout that calculates the total price of a number of items.
An item has the following attributes:
- SKU
- Unit Price

Our goods are priced individually. Some items are multi-priced: buy n of them, and they will cost
you less than buying them individually. For example, item A might cost $50 individually, but this
week we have a special offer: buy three A s and they will cost you $130.

### Pricing Rules

|Item |Unit Price |Special Price|
| --- |:---------:|:-------------|
| A   |   $50      | 3 for $130  |
| B   |   $30      | 2 for $45   |
| C   |   $20      |             |
| D   |   $15      |             |

Our checkout accepts items in any order, so that if we scan a B, an A, and another B, we’ll recognize the two B’s and price them at 45 (for a total price so far of 95). Because the pricing changes frequently, we need to be able to pass in a set of pricing rules each time we start handling a checkout transaction.

### Solution FastAPI Checkout System

This FastAPI application implements a simple checkout system with endpoints for scanning items, retrieving the cart, calculating the total price, and integrated Swagger documentation.

## Functionality

- **Scan Item Endpoint:** `POST /scan/{item_id}`
  - Add an item to the cart.

- **Get Cart Items Endpoint:** `GET /mycart`
  - Retrieve all items in the cart.

- **Calculate Total Price Endpoint:** `GET /total`
  - Calculate the total price of items in the cart.

- **Swagger Documentation:** `/docs`
  - Interactive Swagger UI for API documentation.

## Implementation Details

The main functionality is implemented in `main.py` which includes the following:

- **Checkout Class:** Manages the checkout process, item scanning, and total price calculation based on provided pricing rules.

- **Endpoints:**
  - `/scan/{item_id}`: Adds an item to the cart.
  - `/mycart`: Retrieves items in the cart.
  - `/total`: Calculates the total price of items in the cart.
  - `/docs`: Swagger UI for API documentation.

## Running the Application

1. **Installation:**
   - Ensure Python and pip are installed.

2. **Setup Dependencies:**
   - Install FastAPI and Uvicorn.
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the FastAPI Application:**
   Start the FastAPI server using Uvicorn.
   ```bash
   uvicorn src.main:app --reload

Access the API at http://127.0.0.1:8000 and Swagger UI at http://127.0.0.1:8000/docs.

# Running Tests:
To execute tests, use Pytest. Ensure your server is running before running tests.
```bash
pytest
```

# Folder Structure:
<img width="402" alt="image" src="https://github.com/Gautamaggrawal/supermarket-checkout/assets/22342470/f94b7fb2-0644-4801-a95e-41f496b8e3ef">




