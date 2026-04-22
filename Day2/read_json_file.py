import json

with open("api_data.txt", "r") as f:
    data = json.load(f)

print(data["authorizations_url"])    