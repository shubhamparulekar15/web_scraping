from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from requests_html import HTMLSession
session = HTMLSession()

strLink = "https://www.sdgindex.org"

url = "https://www.sdgindex.org/reports/"
client = uReq(url)
page = client.read() # To read the html of the page
client.close()
pageSoup = soup(page, "html.parser")
links = [] # To store the links of the reports on the page



link_soup = pageSoup.findAll("h3", {"class":"teaser-title"})


for a in range(len(link_soup)):
    link = link_soup[a]
    l = link.find("a")
    link = l["href"]

    if not (link[:6] == "https"):
        link = strLink + link
        links.append(link)




for i in range(len(links)):
    try:
        r = session.get(links[i])
        
        html = r.html.html
        pageSoup = soup(html, "html.parser")
        
        pdf_soup = pageSoup.find("a",{"class":"report-link button large"})
        print(pdf_soup.get('href'))

        
    except :
    
        print("could not download the pdf")