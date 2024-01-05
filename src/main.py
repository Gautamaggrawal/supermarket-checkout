# main.py
from fastapi import FastAPI

from src.checkout import Checkout
from src.constants import pricing_rules
from fastapi.openapi.docs import get_swagger_ui_html


app = FastAPI()
co = Checkout(pricing_rules)

@app.post("/scan/{item_id}")
async def scan_item(item_id: str):
    # Endpoint to scan an item and add it to the cart
    co.scan(item_id)
    return {"message": f"Scanned item: {item_id} successful!"}

@app.get("/mycart")
async def get_mycart():
    # Endpoint to get all the items inside the cart
    cart_items = [{"item": item, "quantity": quantity} for item, quantity in co.cart.items()]
    return {"cart_items": cart_items}


@app.get("/total")
async def get_total():
    # Endpoint to get the total price of all scanned items in the cart
    total_price = co.total()
    return {"total_price": total_price}

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Custom Swagger UI")

@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi()