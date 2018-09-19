import random
from selenium import webdriver
from time import sleep
from Spider_photo import load_page
from Spider_photo import get_image

#自动随机生成登录的手机号和楼盘ID配置
number=random.randint(10,99)
phone=("131000000%s"%number)
id="53061"
#启动浏览器
driver=webdriver.Firefox()
driver.get("https://xf.fangdd.net/baishan")
driver.maximize_window()
print(driver.title)
driver.maximize_window()

#所有元素查找隐式等待5秒
driver.implicitly_wait(5)
#sleep(3)
driver.get("https://xf.fangdd.net/baishan/%s.html"%id)
driver.maximize_window()
print(driver.title)
#未登录领取红包
driver.find_element_by_class_name("discount-item").click()
sleep(1)
driver.find_element_by_class_name("commodal").click()
driver.find_element_by_xpath("/html/body/div[20]/div/div[2]/form/ul/li[1]/input").send_keys("%s"%phone)
sleep(1)
driver.find_element_by_xpath("/html/body/div[20]/div/div[2]/form/ul/li[3]/span").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[20]/div/div[2]/form/ul/li[3]/input").send_keys("111111")
driver.find_element_by_xpath("/html/body/div[20]/div/div[2]/form/button").click()
sleep(2)

print(driver.find_element_by_css_selector("#modalCouponSuccess>div.base-modal>div.cont.modal-main>div.modal-cont>p.success-log").text)
#driver.switch_to_alert().text
sleep(1)
driver.find_element_by_css_selector("#modalCouponSuccess > div.base-modal > div.header > a.modal-close").click()

#driver.refresh()刷新浏览器
#退出
#driver.find_element_by_css_selector("#userInfo.login>a[href='/user/logout']").click()

#登录后报名团购
driver.find_element_by_link_text("立即参团").click()
sleep(1)
#driver.find_element_by_css_selector("#modalCouponSuccess>div.base-modal>div.cont.modal-main>div.modal-cont>p.success-log").screenshot_as_png
sleep(1)
driver.find_element_by_css_selector("#modalGrouponSuccess >div.base-modal >div.header> a.modal-close[href='']").click()
print("团购报名成功")

#跳转买家顾问profile页
#driver.find_element_by_link_text("孙林鹏").click()
#print(driver.find_element_by_class_name("my-service").text)

#driver.close()
#跳转看楼日记页
#跳转户型详情页
#户型详情页领取红包
#户型详情页参与团购

#设置快捷键：Ctrl+Alt+S   多行注释Ctrl+/
# url=("https://xf.fangdd.net/baishan/%s.html"%id)
# html=load_page(url)
# get_image(html)
#截图
#driver.save_screenshot("test.png")


#driver.quit()




