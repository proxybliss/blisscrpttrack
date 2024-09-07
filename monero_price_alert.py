import schedule
import time
from price_checker import get_monero_price
from sms_sender import send_sms
from price_storage import save_price, load_price

phone_number = '+1234567890'

# Function to check the price difference and send alerts if necessary
def check_price():
    current_price = get_monero_price()
    print(f"Current Monero price: ${current_price}")
    
    previous_price = load_price()

    if previous_price:
        price_change_percentage = ((current_price - previous_price) / previous_price) * 100
        print(f"Price change: {price_change_percentage}%")

        # If the price has changed more than 10% (increase or decrease), send an alert
        if abs(price_change_percentage) > 10:
            send_sms(current_price, phone_number)

    # Update the stored price for the next day's comparison
    save_price(current_price)

# Schedule to run every 24 hours (or every hour for testing)
schedule.every(1).days.do(check_price)

while True:
    schedule.run_pending()
    time.sleep(1)
