from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Firefox()
driver.get("http://xf.fangdd.net/shanghai")
sleep(2)
driver.find_element_by_css_selector("#q").send_keys("金地")
#显式等待
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,'search-btn')))
element.click()

sleep(2)
