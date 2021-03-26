from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from requests_html import HTMLSession
from selenium import webdriver

session = HTMLSession()

strLink = "https://www.uneca.org"

url = "https://www.uneca.org/publication-list?field_publication_type_value=All&field_pblication_theme_category_tid=All&field_publication_year_value%5Bvalue%5D=&title="
client = uReq(url)
page = client.read() # To read the html of the page
client.close()
pageSoup = soup(page, "html.parser")
links = [] 

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get(url)
for i in range(2):
	link_soup = pageSoup.findAll("div", {"class":"publicationalltitle"})
	for i in range(len(link_soup)):
		article = link_soup[i].find("a")
		article_link = article["href"]
		# print(article_link)

		if not (article_link[:6] == "https"):
			article_link = strLink + article_link
			links.append(article_link)

	for i in range(len(links)):
	    try:
	        r = session.get(links[i])
	        html = r.html.html
	        pageSoup = soup(html, "html.parser")
	        pdf_soup = pageSoup.find("span",{"class":"file"})
	        pdf_link = pdf_soup.find("a")
	        print(pdf_link.get('href'))
	        print("-------------------------------------------------------------------------")
	    except :
	    
	        print("could not download the pdf")

	driver.find_element_by_link_text("next ›").click()