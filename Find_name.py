#获取楼盘列表全部楼盘名称
from selenium import webdriver
from time import sleep
import xlrd
from selenium.common.exceptions import NoSuchElementException
#启动浏览器
driver=webdriver.Firefox()
driver.get("http://xf.fangdd.net/shanghai")
driver.maximize_window()
sleep(3)
# a=driver.find_elements_by_css_selector("#houseList.house-list>li div.detail>ul>li>span.hsname")
# for i in range(0,len(a)):
#     print(a[i].text)

b=driver.find_element_by_css_selector("#allList.list-all>div.xf-step>a.next")
while b is not None:
    a=driver.find_elements_by_css_selector("#houseList.house-list>li div.detail>ul>li>span.hsname")
    for i in range(0,len(a)):
        print(a[i].text)
    b = driver.find_element_by_css_selector("#allList.list-all>div.xf-step>a.next")
    b.click()


