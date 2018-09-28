import requests
try:
    r = requests.get('https://httpbin.org/ip')
    print("Success reaching address", r)
except requests.exceptions.ConnectionError:
    print("There was an error reaching the specified address.")
