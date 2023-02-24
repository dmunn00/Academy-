from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.edgetesting.co.uk/")
driver.implicitly_wait(20.0)

service_button = driver.find_element(by=By.CLASS_NAME, value="dropdown-toggle")
service_button.click()

managed_testing_button = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Managed")
managed_testing_button.click()


enquire_button = driver.find_element(by=By.CLASS_NAME, value="btn.btn-standard")
enquire_button.click()

title = driver.title
print(title)
