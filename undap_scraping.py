from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import urlopen as uReq
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.undp.org/content/undp/en/home/librarypage/search.html?q=report&tagid=")


url = "https://www.undp.org"


for i in range(3):
 	article_link = driver.find_elements_by_xpath('//div[@class="card-image"]/a')
 	for i in range(len(article_link)):
 		print("---------------------------------------------------------------------------------------------------")
 		time.sleep(1)
 		abc = article_link[i].get_attribute("href")
    	r = session.get(abc)
    	html = r.html.html
 		pageSoup = soup(html, "html.parser")
    	pdf_soup = pageSoup.find_all("ul",{"class":"no-bullet"})
    	pdf_url = pdf_soup[0].li.a.get('href')
    	if("http" in pdf_url):
    		print(pdf_url)
    	else:
        	pdf_url = url+pdf_url
        	print(pdf_url)
 		

 	

 	clz = driver.find_element_by_link_text('Next').click()




