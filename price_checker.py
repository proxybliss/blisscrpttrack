import requests

def get_monero_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data['monero']['usd']
