from selenium import webdriver
from requests_html import HTMLSession
session = HTMLSession()
import time

your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.ghtcoalition.org/resources")

try:
    click_more = True
    while click_more:
        time.sleep(3)
        element = driver.find_element_by_xpath('/html/body/div[4]/main/div/section[1]/div/div/div[3]/div/div[2]/button')
        if element:
            element.click()

            
except:
    click_more = False
    reports = driver.find_elements_by_link_text('PDF')
    for i in range(len(reports)):
    	print(reports[i].get_attribute('href'))

 	

