from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import urlopen as uReq
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.who.int/publications/en/")
article_link = driver.find_elements_by_xpath('//a[@class="buffet_headline"]')
for i in range(len(article_link)):
 		print("---------------------------------------------------------------------------------------------------")
 		abc = article_link[i].get_attribute("href")
 		r = session.get(abc)
 		html = r.html.html
 		pageSoup = soup(html, "html.parser")
 		element = pageSoup.find("li",{"first"})
 		try:
 			pdf_url = element.a.get('href')
 			print(pdf_url)

 		except:
 			print("pdf not found")
 		# try:
 		# 	element = pageSoup.find("li",{"first"})
 		# 	print(element)


 		
 




# try:
#     click_more = True
#     while click_more:
#     	time.sleep(4)
#     	element = driver.find_element_by_class_name('owl-next').click()
#     	if element:
#     		element.click()
#     		article_link = driver.find_elements_by_xpath('//div[@class="field-content"]/a')


            

    