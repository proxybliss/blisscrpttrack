from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

def send_sms(price, phone_number):
    message = client.messages.create(
        body=f"Monero price alert: The price has changed by more than 10%. Current price is ${price}",
        from_='+your_twilio_phone_number',
        to=phone_number
    )
    print(f"Sent message: {message.sid}")
