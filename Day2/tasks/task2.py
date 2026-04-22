#Task 2
#Read file and print

import json

with open("api_data.txt", 'r') as f:
    data = json.load(f)
    print(data["current_user_url"])

