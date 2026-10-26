import requests
import json

base_url = "https://swapi.dev/api/"
endpoint = "people/5"

response = requests.get(base_url + endpoint)
data = response.json()
# print(data)
print(data['name'])
#print(data['results'][0]['name']) 
# print(response)
# print("Text:")
# print(response.text)
# print("Status Code:")
# print(response.status_code)
# print("Headers:")
# print(response.headers)