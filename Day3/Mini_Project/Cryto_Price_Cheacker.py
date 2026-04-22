# import requests

# coin = input("Enter coin name (bitcoin/etherum): ").lower()

# url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

# response = requests.get(url)
# data = response.json()

# print(data)

#this will fail when the input will other than the given bcoz The API accepted "abc" as a valid coin
#The CoinGecko API:
# Doesn’t strictly validate names like you think
# Sometimes matches similar or unknown tokens
# Returns data even for weird inputs
# if coin in data and "usd" in data[coin]:
#     print(f"{coin} price is: ", data[coin]["usd"], "USD")
# else: 
#     print("Invalid coin name")    


import requests

coin = input("Enter coin name (bitcoin/ethereum): ").lower()

valid_coins = ["bitcoin", "ethereum"]

if coin not in valid_coins:
    print("Invalid coin name")
else:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    
    response = requests.get(url)
    data = response.json()

    print(data)
    print(f"{coin} price is:", data[coin]["usd"], "USD")

    if response.status_code == 200:
       data = response.json()
       print(f"{coin} price is:", data[coin]["usd"], "USD")
    else:
         print("API error")    
