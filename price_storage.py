import json
import os

PRICE_FILE = 'price_data.json'

# Save the current price to a file
def save_price(price):
    with open(PRICE_FILE, 'w') as f:
        json.dump({'price': price}, f)

# Load the previous price from a file
def load_price():
    if os.path.exists(PRICE_FILE):
        with open(PRICE_FILE, 'r') as f:
            data = json.load(f)
            return data['price']
    return None  # If the file doesn't exist, return None
