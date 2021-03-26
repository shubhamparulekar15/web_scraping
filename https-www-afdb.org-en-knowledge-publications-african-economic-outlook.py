from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from requests_html import HTMLSession
from selenium import webdriver

session = HTMLSession()

strLink = "https://www.afdb.org/"

url = "https://www.afdb.org/en/knowledge/publications/african-economic-outlook"
client = uReq(url)
page = client.read() # To read the html of the page
client.close()
pageSoup = soup(page, "html.parser")
links = [] 

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get(url)
for i in range(2):
	link_soup = pageSoup.findAll("td", {"class":"views-field views-field-title"})
	for i in range(len(link_soup)):
		article = link_soup[i].find("a")
		article_link = article["href"]
		
		if not (article_link[:6] == "https"):
			article_link = strLink + article_link
			links.append(article_link)
	print(links)
	print("-------------------------------------------------------------------------")
	# driver.find_element_by_link_text("next ›").click()
