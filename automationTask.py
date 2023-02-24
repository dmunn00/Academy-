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
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.edgetesting.co.uk/")
driver.implicitly_wait(10.0)

Service_button = driver.find_element(by=By.CLASS_NAME, value="dropdown-toggle")
Service_button.click()

ManagedTesting_button = driver.find_element(by=By.LINK_TEXT, value="Managed Testing")
ManagedTesting_button.click()

div=driver.find_element(By.CLASS_NAME, value="centerblock")
Enquire_button = div.find_element(by=By.XPATH, value="a[1]")
Enquire_button.click()


Name_field = driver.find_element(by=By.ID, value="ContentPlaceHolderDefault_Content_contact_4_txtContactName")
Name_field.send_keys("Ada")

PhoneNo_field = driver.find_element(by=By.ID, value="ContentPlaceHolderDefault_Content_contact_4_txtContactEmail")
PhoneNo_field.send_keys("1234567")

Email_field = driver.find_element(by=By.ID, value="ContentPlaceHolderDefault_Content_contact_4_txtContactPhone")
Email_field.send_keys("hello.hello@email.com")

Message_field = driver.find_element(by=By.ID, value="ContentPlaceHolderDefault_Content_contact_4_txtContactMessage")
Message_field.send_keys("Have a nice day!")
time.sleep(10)



