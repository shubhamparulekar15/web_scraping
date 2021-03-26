from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import Request, urlopen 
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.africa-energy.com/special-reports")

url = "https://www.africa-energy.com"
article_link = driver.find_elements_by_link_text('view')
for i in range(len(article_link)):
	print("---------------------------------------------------------------------------------------------------")
	abc = article_link[i].get_attribute("href")
	r = session.get(abc)
	html = r.html.html
	pageSoup = soup(html, "html.parser")
	pdf_soup = pageSoup.find("div",{"class":"field field-name-body field-type-text-with-summary"})
	x = pdf_soup.find_all("a")
	for i in range(1):
		print(x[0].get("href"))
