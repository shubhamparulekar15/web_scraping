from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from requests_html import HTMLSession
from selenium import webdriver
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
session = HTMLSession()

strLink = "https://acetforafrica.org"
url = "https://acetforafrica.org/publication_type/reports"
# client = uReq(url)
# page = client.read() # To read the html of the page
# client.close()
# # r = session.get(url)
# #         # r.html.render()
# # html = r.html.html
# pageSoup = soup(page, "xml")
links = [] 

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get(url)


# for i in range(2):
link_soup = driver.find_elements_by_class_name("card-title")
for i in range(len(link_soup)):
	print("---------------------------------------------------------------------------------------------------")
	article_link = link_soup[i].get_attribute('href')
	client = uReq(url)
	page = client.read() # To read the html of the page
	client.close()
	# r = session.get(article_link)
	# html = r.html.html
	pageSoup = soup(page, "html.parser")
	# pdf_url = pdf_soup[1].a.get('href')
	print(len(pdf_soup))
# r = session.get(article_link)
# html = r.html.html
# client1 = uReq(article_link)
# page1 = client.read() # To read the html of the page
# client1.close()
# pageSoup1 = soup(page1, "html.parser")
# pdf_soup = pageSoup1.findAll("div",{"class":"section_wrapper"})
# pdf_link = pdf_soup.a.get("href")
# print(len(pdf_soup))
		
	# print(links)
	# print("-------------------------------------------------------------------------")
	# driver.find_element_by_link_text("Next page").click()