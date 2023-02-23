from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://www.easyjet.com/en")

title = driver.title

driver.implicitly_wait(10.0)

cookie = driver.find_element("id","ensCloseBanner")
cookie.click()

from_box = driver.find_element("name", value="origin")
from_box.send_keys(Keys.CONTROL + "a")
from_box.send_keys(Keys.DELETE)

from_box.send_keys("Birmingham")

from_box.send_keys(Keys.ENTER)

to_box = driver.find_element("name", value="destination")
to_box.send_keys(Keys.CONTROL + "a")
to_box.send_keys(Keys.DELETE)

to_box.send_keys("Glasgow")
driver.implicitly_wait(10.0)
to_box.send_keys(Keys.ENTER)

#departingDate = driver.find_element("css_selector","routedatepicker-83050")
#departingDate.click()
#departingDate = driver.find_element("className","date-picker-button button-reset")
#departingDate.click()

#submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
driver.implicitly_wait(10.0)
#driver.quit()