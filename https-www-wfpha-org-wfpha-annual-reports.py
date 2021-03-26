from selenium import webdriver
your_exec_path = r"C:\Users\PARULEKAR\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=your_exec_path)
driver.get("https://www.wfpha.org/publications/wfpha-annual-reports")
articles = driver.find_elements_by_xpath('//*[@id="div_sflcontent"]/div/div/div/nobr/a')
for i in range(len(articles)):
	print("-----------------------------------------------------------------------------------------------------------")
	print(articles[i].get_attribute('href'))
