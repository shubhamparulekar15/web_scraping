from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession
session = HTMLSession()
url_start = "https://www.csis.org/"
url = "https://www.csis.org/analysis?type=publication&field_publication_type%5B1%5D=781&page="
for i in range(359):
	print("---------------------------------------------------------------------------------------------------")
	print(i)
	main_page_url =  url+str(i)
	main_r = session.get(main_page_url)
	main_html = main_r.html.html
	main_pageSoup = soup(main_html, "html.parser")
	article_link = main_pageSoup.find_all("div",{"class":"teaser__title"})
	for art in article_link:
		art_link = url_start+art.a.get("href")
		r = session.get(art_link)
		html = r.html.html
		pageSoup = soup(html, "html.parser")
		pdf_soup = pageSoup.find("a",{"class":"button button--primary"})
		if pdf_soup:
			pdf_url = pdf_soup.get('href')
			print(pdf_url)

