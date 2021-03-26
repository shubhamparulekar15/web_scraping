from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession
session = HTMLSession()
import time

url_start = "https://www.kff.org/"

url = "https://www.kff.org/search/?s&fs=search&orderby&tab&layout&facets[start_date]&facets[end_date]&facets[post_type][0]=report&paged="


for i in range(15,30):

	print("---------------------------------------------------------------------------------------------------")
	print(i)

	main_page_url =  url+str(i)
	main_r = session.get(main_page_url)
	main_html = main_r.html.html
	main_pageSoup = soup(main_html, "html.parser")




	article_link = main_pageSoup.find_all("h5")
	for art in article_link:
		art_link = url_start+art.a.get("href")
		# print(art_link)
		r = session.get(art_link)
		html = r.html.html
		pageSoup = soup(html, "html.parser")
		pdf_soup = pageSoup.find("section",{"class":"feature attachments"})
		pdf_soup1 = pageSoup.find("div",{"class":"box full-post"})
		if pdf_soup:
			pdf_url = pdf_soup.ul.li.a.get('href')
			print(pdf_url)

		if pdf_soup1:
			pdf_url1 = pdf_soup1.p[-1].a.get('href')
			print(pdf_url1)
			
		

	# 	a = driver.find_element_by_link_text('Next page').click()
# https://www.kff.org/search/?s=&fs=search&orderby=&tab=&layout=&facets[start_date]=&facets[end_date]=&facets[post_type][]=report
# https://www.kff.org/search/?s&fs=search&orderby&tab&layout&facets[start_date]&facets[end_date]&facets[post_type][0]=report&paged=100