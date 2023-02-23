from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.edgetesting.co.uk/")

title = driver.title

driver.implicitly_wait(1.0)

Service_button = driver.find_element(by=By.CLASS_NAME, value="dropdown-toggle")
Service_button.click()

TestAutomation_button = driver.find_element(by=By.LINK_TEXT, value="Test Automation")
TestAutomation_button.click()

#automationButton = driver.find_element(by=By.CLASS_NAME, value="active")
#automationButton.click()
title = driver.title
print(title)

