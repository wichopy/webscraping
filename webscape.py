##Abandoned this file. Was too difficult reading raw html data using the method of terminal + sublime as suggested. 
#Instead implemented code in jupyter notbook for more clarity.

from urllib import  as urlopen as UReq
from bs4 import BeautifulSoup as soup
my_url = "https://www.expedia.ca/Deals"

uClient = urllib.urlopen(my_url)

page_html = uClient.read()
uClient.close()

#next parse HTML
"""
Once in beautiful soup we can traverse it.
"""
