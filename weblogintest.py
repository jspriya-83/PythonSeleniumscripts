from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("./chromedriver")

driver.get("http://www.linkedin.com")

element=driver.find_element_by_link_text("Sign in")
element.click()
time.sleep(10)

email=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
signin_button=driver.find_element_by_tag_name("button")
email.send_keys("jspriya_83@yahoo.co.in")
password.send_keys("Riya0106")
signin_button.click()
time.sleep(10)


driver.close()
