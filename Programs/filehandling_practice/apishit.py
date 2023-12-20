import pip._vendor.requests as requests
url = str("https://api.dictionaryapi.dev/api/v2/entries/en/")

while True:
    word = input()
    newurl = url+word
    data = requests.get(newurl)
    print(data.status_code)
    print(data)
