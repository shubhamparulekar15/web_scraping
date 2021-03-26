from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import urlopen as uReq
session = HTMLSession()
r = session.get("https://www.wma.net/publications/wma-annual-report/")
html = r.html.html
pageSoup = soup(html, "html.parser")
pdf_soup = pageSoup.find_all("a",{"target":"_blank"})
for i in range(len(pdf_soup)):
	print(pdf_soup[i].get('href'))
# print(len(pdf_soup))