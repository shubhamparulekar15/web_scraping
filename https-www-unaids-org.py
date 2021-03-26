
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import urlopen as uReq
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.unaids.org/en/resources/publications/all")

try:
    click_more = True
    while click_more:
        time.sleep(4)
        element = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/ul/li/a')
        if element:
            element.click()

            
except:
    click_more = False
    article_link = driver.find_elements_by_xpath('//div[@class="field-content"]/a')
    for i in range(len(article_link)):
    	print("---------------------------------------------------------------------------------------------------")
    	time.sleep(1)
    	abc = article_link[i].get_attribute("href")
    	r = session.get(abc)
    	html = r.html.html
    	pageSoup = soup(html, "xml")
    	pdf_soup = pageSoup.find_all("div",{"block-inner"})
    	pdf_url = pdf_soup[0].p.a.get('href')
    	print(pdf_url)

