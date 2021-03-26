from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import urlopen as uReq
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://openknowledge.worldbank.org/browse?type=title")
url = "https://openknowledge.worldbank.org/"

for i in range(10):
    try:
    	time.sleep(5)
    	article_link = driver.find_elements_by_xpath('//div[@class="content"]/h4/a')
    	for i in range(len(article_link)):
    		abc = article_link[i].get_attribute("href")
    		r = session.get(abc)
    		html = r.html.html
    		pageSoup = soup(html, "html.parser")
    		element = pageSoup.find("a",{"bitstream-link"})
    		pdf_url = element.get('href')
    		if("http" in pdf_url):
    			print(pdf_url)
    		else:
    			pdf_url = url+pdf_url
    			print(pdf_url)








    	next_page_button = driver.find_element_by_link_text('>>').click()
            
    except:
        print("------------------------------------------------------------")
        # print(a)
        # print("error aaya re")
        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[4]/button[2]').click()