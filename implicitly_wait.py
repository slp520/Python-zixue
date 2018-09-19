from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime

driver=webdriver.Firefox()
driver.get("http://xf.fangdd.net/shanghai")
sleep(2)
#隐式等待
driver.implicitly_wait(5)
try:
    print(ctime())
    driver.find_element_by_css_selector("#q").send_keys("金地")
    driver.find_element_by_class_name("search-btn").click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())

