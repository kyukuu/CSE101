import requests

api_key = "d294017e48310beb66eb43b6a5bd6f8e"
loc = "Sydney"
url = f"http://api.openweathermap.org/geo/1.0/direct?q={loc}&appid={api_key}"


print(url)
resp = (requests.get(url))

if resp.status_code == 200:
    data = resp.json()

    for i in data:
        print(i["lat"])
        print(i["lon"])
else:
    print("request failed, status code:", resp.status_code)
