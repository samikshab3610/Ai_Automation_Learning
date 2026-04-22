import requests

coin = input("Enter coin name (bitcoin/ethereum): ").lower()

valid_coins = ["bitcoin", "ethereum"]

if coin not in valid_coins:
    print("Invalid coin name")
else:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"{coin} price is:", data[coin]["usd"], "USD")
    else:
        print("API error")