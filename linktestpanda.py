from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests

driver=webdriver.Chrome("./chromedriver")
driver.get("https://www.google.com")

search=driver.find_element_by_name("q")
search.send_keys("Home remedies for cough and cold")
search.send_keys(Keys.RETURN)

links=[]
hrefs=[]
status=[]

links=driver.find_elements_by_tag_name("a")
print(len(links))
for link in links:
    href=(link.get_attribute('href'))
    if(str(href)!="None"):
        hrefs.append(href)
        r=requests.head(href)
        status.append(r)


df=pd.DataFrame(list(zip(hrefs,status)),columns=['Links','Status'])
df.to_csv("/home/rampriya/Documents/Venture2020/firsttest.csv")
#print(df)
driver.quit()




