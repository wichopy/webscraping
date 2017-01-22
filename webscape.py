from urllib import  as urlopen as UReq
from bs4 import BeautifulSoup as soup
my_url = "https://www.expedia.ca/Deals"

uClient = urllib.urlopen(my_url)

page_html = uClient.read()
uClient.close()

#next parse HTML
page_soup=soup(page_html, "html.parser")

"""
Once in beautiful soup we can traverse it.
"""
page_soup.ffindAll(<div class="box tile-details "> <p class="secondary tile-price" id="tile-hotel-price-0-0-1"> <strong id="hotel-price-0-0-1"> C$48 </strong> <br>per night<br> <span class="cross-out-price" id="cross-out-price-0-0-1"></span> </p> <h4 class="tile-name" id="tile-hotel-name-0-0-1">Hotel only</h4> <p class="secondary">Thu, 23 Feb - Sun, 26 Feb</p> </div>)