import requests

def get_crypto_price():
    coin = input("Enter coin name (bitcoin/ethereum): ").lower()

    valid_coins = ["bitcoin", "ethereum"]

    if coin not in valid_coins:
        print("Invalid coin name")
        return

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    try:
        response = requests.get(url, timeout= 5)

        if response.status_code != 200:
            print("API error:", response.status_code)
            return  # 🔥 STOP HERE

        data = response.json()

        print(f"{coin} price is:", data[coin]["usd"], "USD")

    except requests.exceptions.ConnectionError:
        print("No internet connection")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except KeyError:
        print("Unexpected data format")


get_crypto_price()