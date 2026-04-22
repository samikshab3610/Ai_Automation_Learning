import requests
import json

url = "https://api.github.com"

response = requests.get(url)
data = response.json()

#save this to file
with open("api_data.txt", 'w')as f:
    json.dump(data, f, indent=4)