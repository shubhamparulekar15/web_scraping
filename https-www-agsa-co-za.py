from bs4 import BeautifulSoup as soup
from selenium import webdriver
from requests_html import HTMLSession
from urllib.request import urlopen as uReq
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.agsa.co.za/Reporting/AnnualReport.aspx")

url = "https://www.agsa.co.za/Reporting/AnnualReport.aspx"
links = [] # To store the links of the reports on the page
page_no = driver.find_element_by_xpath('//*[@id="dnn_ctr603_Repository_FooterTable"]/tbody/tr/td/table/tbody/tr/td/span[3]').text


for i in range(int(page_no)):
	link_soup = driver.find_elements_by_link_text('DOWNLOAD')
	for a in link_soup:
		links.append(a.get_attribute("href"))
	driver.find_element_by_xpath('//*[@title="Click to view the next page"]').click()
	
print(links)