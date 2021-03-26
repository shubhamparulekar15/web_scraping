from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import urlopen as uReq
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.iea.org/analysis/all?type=report")
# count =0

url = "https://www.iea.org"
# t = driver.find_element_by_xpath('//*[@id="library-results-1612542668"]/nav/ul/li[11]/a')

# for i in range(3):
article_link = driver.find_elements_by_class_name('m-analysis-listing__link')
for i in range(len(article_link)):
    # print("---------------------------------------------------------------------------------------------------")
    abc = article_link[i].get_attribute("href")
    r = session.get(abc)
    html = r.html.html
    pageSoup = soup(html, "xml")
    pdf_soup = pageSoup.findAll("a",{"class":"a-link a-link--accent"})
    print(len(pdf_soup))
