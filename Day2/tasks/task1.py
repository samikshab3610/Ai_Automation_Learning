# Save API data to file
# Open file manually and check

import requests
import json

url = 'https://api.freeapi.app/api/v1/public/randomjokes/joke/random'

response = requests.get(url)
data = response.json()
#print(data)

# save to  file 
# with open("random_jokes.txt", 'w') as f:
#     json.dump(data, f, indent=4)


#two ways to read the api json

#1st 
# Read from file correctly
# with open('random_jokes.txt', 'r') as f:
#     data = json.load(f)   # <-- IMPORTANT

# print(data['data']['content'])


#2nd
# with open('random_jokes.txt', 'r') as f:
#     data = json.loads(f.read())

#     print(data['data']['content'])    



