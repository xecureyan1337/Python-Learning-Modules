import requests

urls = ["https://eknows.uinsgd.ac.id", "https://eknows.uinsgd.ac.id/config.js", "https://salamas.uinsgd.ac.id/"]

for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print("got you")
    except Exception as er:
        print(f"Oopsss, error: {er}")
    else:
        print("Voila..")