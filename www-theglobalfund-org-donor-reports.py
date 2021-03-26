from selenium import webdriver
your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.theglobalfund.org/en/publications/donor-reports/")
url = "https://www.theglobalfund.org"
articles = driver.find_elements_by_xpath('//*[@id="13941"]/li/small/a')
for i in range(len(articles)):
	print("-----------------------------------------------------------------------------------------------------------")
	print(articles[i].get_attribute('href'))


