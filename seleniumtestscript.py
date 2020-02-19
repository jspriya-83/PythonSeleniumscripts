from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#creating a new  chrome session

chrome_options=webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches",['enable-automation']);


driver=webdriver.Chrome("./chromedriver",options=chrome_options);
driver.implicitly_wait(30)
driver.maximize_window()


driver.get("http://www.google.com")
element=driver.find_element_by_name("q")

element.send_keys("Home remedies for cold and cough")
element.submit()


lists=driver.find_elements_by_class_name("r")

print("Returned "+str(len(lists))+" website links")

i=0

for item in lists:
    print(item.get_attribute("innerHTML"))
    i=i+1
    if(i>10):
        break

driver.quit()


