from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import urlopen as uReq
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("http://www.adry.up.ac.za/")
url = "https://www.atlanticcouncil.org"

articles = driver.find_elements_by_xpath('//*[@class="rt-image rt-attribution"]/a')
for i in range(len(articles)):
	abc = articles[i].get_attribute("href")
	r = session.get(abc)
	html = r.html.html
	pageSoup = soup(html, "html.parser")
	pdf_soup = pageSoup.find("a",{"target":"_blank"})
	if(pdf_soup == None):
		print("PDF NOT FOUND")
		continue
	pdf_url = pdf_soup.get('href')
	pdf_url = url+pdf_url
	print(pdf_url)



# while(click_button):
# 	click_button.click()

