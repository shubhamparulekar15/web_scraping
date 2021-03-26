from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
session = HTMLSession()


pdf_origin = "https://www.pwc.co.tz"

r = session.get('https://www.pwc.co.tz/publications.html')
r.html.render()

html = r.html.html

page_soup = BeautifulSoup(html, 'html.parser')

soup2 = page_soup.find_all('article',{"class":"col-sm-4 col-md-3 col-xs-6 collection__item feedItem ng-scope"})

for article in soup2:

    txt = article.find_all('span',{"class":"ng-binding"})
    date = article.find_all('time',{"class":"ng-binding"})
    # art_link = article.find_all('a',{"class":"collection__item-link inheritColor ng-scope"})
	# art_link = art_link[0].get("href")
	# # cta-download__link
	# r2 = session.get(art_link)
    # r2.html.render()
	# html2 = r2.html.html
	# page_soup_2 = BeautifulSoup(html2, 'html.parser')
	# soup3 = page_soup_2.find_all('a',{"class":"cta-download__link"})
	# if(len(soup3) >0):
    # # print(soup3[0].get("href"))
    #     pdf_link = pdf_origin+soup3[0].get("href")
    # else:
    #     pdf_link = None

    print(txt[0].text," | ",date[0].text)
