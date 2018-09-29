#open webpage
#strip out the IP from the requests command
#open webbrowser and query google

import webbrowser, requests, sys

try:
    #get data from website
    r = requests.get('https://httpbin.org/ip')
    #debugging #print (r.text)
    #err = requests.exceptions.RequestException()
    #print(requests.RequestException())
    #print(err)
#except requests.exceptions.ConnectionError:
except:
    sys.exit(1)
    
#store this as a dictionary
s=r.json()

#debugging print type(s)
#debugging print s
#debugging print (s.[1])
#debugging print s["origin"]

#lookup the result from the key "origin", convert from unicode to string
IP=str(s["origin"])

print (IP)

webbrowser.open("http://www.google.com/search?q=ip locator " + IP)


    


