from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver=webdriver.Firefox()
driver.get("http://xf.fangdd.net/shanghai")
driver.maximize_window()
driver.find_element_by_css_selector("#q").send_keys("金地")
driver.find_element_by_css_selector("#q").send_keys(Keys.CONTROL,'a')
sleep(2)
driver.find_element_by_css_selector("#q").send_keys(Keys.CONTROL,'x')
driver.find_element_by_css_selector("#q").send_keys(Keys.CONTROL,'v')
