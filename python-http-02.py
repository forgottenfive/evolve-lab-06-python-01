import requests
import webbrowser
try:
    r = requests.post('https://httpbin.org/post', data = {'key':'value'})
    json_info = r.json()
    print("Success reaching address", json_info['origin'])
except requests.exceptions.ConnectionError:
    print("There was an error reaching the specified address. Exiting.")
    exit()

if str(input("Continue to google ip locator? (Yn) ")).lower() != "y":
    exit()
else:
    try:
        url = 'https://www.google.com/search?q=ip locator ' + str(json_info['origin'])
        webbrowser.open(url)
    except:
        print("There was an error locating your ip with google ip locator. Exiting.")
        exit()
