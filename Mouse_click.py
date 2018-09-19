from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Firefox()
driver.get("http://xf.fangdd.net/shanghai")
driver.maximize_window()
driver.find_element_by_css_selector("#q").send_keys("金地")
element=driver.find_element_by_css_selector("#q")
#双击操作
ActionChains(driver).double_click(element).perform()
sleep(2)
#右击
ActionChains(driver).context_click(element).perform()
#s鼠标悬停
above=driver.find_element_by_css_selector(".more")
ActionChains(driver).move_to_element(above).perform()
sleep(3)


