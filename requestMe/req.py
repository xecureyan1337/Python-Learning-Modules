import requests

# get requests
url = "https://eknows.uinsgd.acx.ixd"

response = requests.get(url)
# print(response)

# status_code
# print(response.status_code)

if response.status_code == 200:
    print("Authenticated")
elif response.status_code == 404:
    print("Not Found")