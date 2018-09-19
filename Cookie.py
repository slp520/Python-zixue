from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://shop.fangdd.net/house/summary_list.html")
driver.maximize_window()

#获取cookie全部内容
cookie=driver.get_cookies()
#打印全部cookile信息
print(cookie)
#打印cookie第一组信息
print(cookie[0])

#添加cookie
driver.add_cookie({'name':'新体验项目助理','value':'Fdd123@@'})
for cookie in driver.get_cookies():
    print("%s --- %s" %(cookie['name'],cookie['value']))
