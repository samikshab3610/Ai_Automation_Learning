import requests
import json

url = "https://api.github.com"

response = requests.get(url)
data = response.json()

#save

with open("api_data", 'w') as f:
    json.dump(data, f, indent=4)

#read
with open("api_data", 'r') as f:
    loaded_data = json.load(f)

print("Auth URL: ", loaded_data["authorizations_url"]) 
print("Current User URL: ", loaded_data["current_user_url"])
print(loaded_data["events_url"])  