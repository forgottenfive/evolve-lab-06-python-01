import bs4, requests, sys

try:
    res=requests.get('http://www.example.com/')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #type(soup)
    #print soup.prettify() #debugging
    #soup.tag.decompose() #debugging
    #print soup.find_all('p') #debugging
    #print (soup.p) #debugging
except requests.exceptions.RequestException:
    sys.exit(1)
#returns a result set (bs4 list?) 
#pg=soup.find_all('p')

#returns the first paragraph
pg=soup.find('p')
#print (pg.text) #prints tect only of object
#print type(pg)

file = open("example.txt", "w")
file.write(pg.text)
file.close

      
#print soup.find("h1")  #debugging
#cshow each item in the resultset #debugging
#for thing in pg:   #debugging
#    print (thing.text) #debugging

#soup.select('<p>')
#type(soup.select('h1'))  #returns lists
#h1list= soup.select('h1')
#for elm in h1list:
#    print (elm)
