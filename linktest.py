from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import pandas as pd


driver=webdriver.Chrome("./chromedriver")
driver.implicitly_wait(30)
driver.get("http://www.google.com")


search=driver.find_element_by_name("q")
search.send_keys("home remedies for cold and cough")
search.send_keys(Keys.RETURN)

links=[]
href=[]

links=driver.find_elements_by_tag_name("a")
length=len(links)
print(type(links))
for link in links:
    if(str(link.get_attribute('href'))!="None"):
        r=requests.head(link.get_attribute('href'))
        print(str(link.get_attribute('href')),r)
#print(href)

print(len(links))

