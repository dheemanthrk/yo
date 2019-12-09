from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url="https://www.amazon.in"

search_term=input ('What do you want to search for in amazon ?')

driver=webdriver.Chrome(executable_path=r'C:/Users/dheem/Downloads/chromedriver_win32/chromedriver.exe')

driver.maximize_window()

driver.implicitly_wait(10) #10 is in seconds

driver.get(base_url)

assert "Amazon" in driver.title

searchTextBox=driver.find_element_by_id("twotabsearchtextbox")

searchTextBox.clear()

searchTextBox.send_keys(search_term)

searchTextBox.send_keys(Keys.RETURN)

assert f"Amazon.in:{search_term}" in driver.title

assert "No results found." not in driver.page_source

driver.close()