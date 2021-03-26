from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
session = HTMLSession()

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.ghtcoalition.org/resources")
article_link = driver.find_elements_by_xpath('//*[@align="center"]/p/a')
for i in range(len(article_link)):
	print(article_link[i].get_attribute('href'))



 		
 




