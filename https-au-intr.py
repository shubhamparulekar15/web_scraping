from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import urlopen as uReq
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://au.int/en/reports")
url = "https://au.int"

for i in range(100):
	time.sleep(3)
	article_link = driver.find_elements_by_xpath('//span[@class="field-content"]/a')
	for i in range(len(article_link)):
		print("---------------------------------------------------------------------------------------------------")
		time.sleep(3)
		abc = article_link[i].get_attribute("href")
		r = session.get(abc)
		html = r.html.html
		pageSoup = soup(html, "html.parser")
		pdf_soup = pageSoup.find("span",{"class":"file"})
		pdf_url = pdf_soup.a.get('href')
		print(pdf_url)

	clz = driver.find_element_by_link_text('next ›').click()