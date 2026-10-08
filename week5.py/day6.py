
import requests
# Fetch a public API and print the response

url = "https://httpbin.org/org"

response = requests.get(url)

print(response.status_code)    #200
data = response.json()         #converts JSON to python dict
print(data["follower"])                #120000




