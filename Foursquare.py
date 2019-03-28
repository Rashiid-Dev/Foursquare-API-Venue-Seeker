import json
import requests
import csv

url = 'https://api.foursquare.com/v2/venues/explore'

CLIENT_ID = 'ULD1MG0DG1Y1EB2APLJ4XZWIDHZ2OI4OYLUKULPRVVSIJJC0'
CLIENT_SECRET = 'P2CHGT1SEU0EXKVQZCUJPCVQWXBS5W0I0UTUQ0YLAHCJTQHK'
print("\nWelcome to Venue Seeker with Foursquare\n")
place = input("Where would you like to search? \n - ")
Query = input("\nWhat item would you like to search for? \n - ")
params = dict(
    client_id='ULD1MG0DG1Y1EB2APLJ4XZWIDHZ2OI4OYLUKULPRVVSIJJC0',
    client_secret='P2CHGT1SEU0EXKVQZCUJPCVQWXBS5W0I0UTUQ0YLAHCJTQHK',
    v='20180323',
    near=place,
    query=Query,
    limit=5
)

response = requests.get(url=url, params=params)
data = json.loads(response.text)
init = (data["response"])
print(init)

f = open("Venue Data.txt", 'w+')
f.write(str(init))
f.close()

# print(init[1])
# for items in data['response']:
#     print(items)
