import requests

urls = [
    "https://salam.uinsgd.ac.id",
    "https://ict.uinsgd.ac.id"
]

for url in urls:
    try:
        response = requests.get(url)
    except Exception as err:
        print(f"Oppss... Error: {err}")
    else:
        if response.status_code == 200:
            print(response.content)
        elif response.status_code == 404:
            print("Not Found")
        else:
            print("Redirect to the url")