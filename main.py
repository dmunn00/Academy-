from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.edgetesting.co.uk/")
driver.implicitly_wait(10.0)

Service_button = driver.find_element(by=By.CLASS_NAME, value="dropdown-toggle")
Service_button.click()

# Service_list = driver.find_element(by=By.CLASS_NAME, value="dropdown-menu")
TestAutomation_button = driver.find_element(by=By.LINK_TEXT, value="Test Automation")
TestAutomation_button.click()

WritingBlock = driver.find_element(by=By.CLASS_NAME, value='widecenterblock')
Result = driver.find_element(by=By.TAG_NAME, value="h3")
print(Result.text)

