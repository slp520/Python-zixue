from selenium import webdriver
from time import sleep
import random
import os




#链接
driver = webdriver.Firefox()
base_url = "http://shop.fangdd.net/login.html"
driver.get(base_url)
driver.maximize_window()
driver.implicitly_wait(30)
#登录

driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys(u"新体验项目助理")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("Fdd123@@")
driver.find_element_by_id("refresh-code").click()
driver.find_element_by_id("code").clear()
SecretCode = input("please enter the code: ")
driver.find_element_by_id("code").send_keys(SecretCode)
driver.find_element_by_id("Js-login").click()
#基本信息

id = random.randint(100, 1000)
driver.implicitly_wait(30)
driver.find_element_by_link_text(u"体验公司").click()
sleep(3)
driver.find_element_by_link_text(u"资金管理").click()
driver.find_element_by_css_selector("span.nav-text").click()
driver.find_element_by_link_text(u"楼盘列表").click()
driver.find_element_by_css_selector("button.ant-btn").click()
#基本信息
driver.find_element_by_id("houseName").clear()
driver.find_element_by_id("houseName").send_keys(u"小木鸟楼盘%s"%id)
driver.find_element_by_id("houseOtherName").clear()
driver.find_element_by_id("houseOtherName").send_keys(u"无")
driver.find_element_by_id("cityTreeCascader").click()
driver.find_element_by_id("cityTreeCascader").clear()
driver.find_element_by_id("cityTreeCascader").send_keys(u"深圳")
driver.find_element_by_css_selector("li.ant-cascader-menu-item.ant-cascader-menu-item-expand").click()
driver.find_element_by_xpath("//ul[2]/li").click()
driver.find_element_by_xpath("//ul[3]/li[2]").click()
#地图标识
driver.find_element_by_id("houseAddress").clear()
driver.find_element_by_id("houseAddress").send_keys(u"深圳南山科技园")
driver.find_element_by_css_selector("button.ant-btn.ant-btn-sm").click()
driver.find_element_by_css_selector(
    "form.ant-form.ant-form-inline > div.ant-row.ant-form-item > div.ant-form-item-control-wrapper > div.ant-form-item-control.has-success > span.ant-input-group-wrapper > span.ant-input-wrapper.ant-input-group > span.ant-input-group-addon > button.ant-btn.ant-btn-sm").click()
driver.find_element_by_xpath("(//button[@type='button'])[5]").click()

driver.find_element_by_id("houseAreaAll").clear()
driver.find_element_by_id("houseAreaAll").send_keys("111")
driver.find_element_by_id("houseAreaBuild").clear()
driver.find_element_by_id("houseAreaBuild").send_keys("111")
driver.find_element_by_id("housePlotRatio").clear()
driver.find_element_by_id("housePlotRatio").send_keys("1")
driver.find_element_by_id("houseCoveredRatio").clear()
driver.find_element_by_id("houseCoveredRatio").send_keys("12")
driver.find_element_by_id("houseHouseholds").clear()
driver.find_element_by_id("houseHouseholds").send_keys("123")
driver.find_element_by_id("houseParkingOverground").clear()
driver.find_element_by_id("houseParkingOverground").send_keys("123")
driver.find_element_by_id("houseParkingUnderground").click()
driver.find_element_by_id("houseParkingUnderground").clear()
driver.find_element_by_id("houseParkingUnderground").send_keys("123")
driver.find_element_by_id("housePropertyCompany").clear()
driver.find_element_by_id("housePropertyCompany").send_keys(u"测试物业")
#推荐理由
#driver.find_element_by_id("houseRecommendedReason").clear()
#driver.find_element_by_id("houseRecommendedReason").send_keys(u"测试的理由")
#点击保存
#driver.find_element_by_css_selector("button.ant-btn.ant-btn-primary").click()
#点击下一步
driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
sleep(3)
driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
#配套信息

#配套信息
driver.find_element_by_id("trafficSupport").clear()
driver.find_element_by_id("trafficSupport").send_keys(u"测试")
driver.find_element_by_id("schoolSupport").clear()
driver.find_element_by_id("schoolSupport").send_keys(u"测试")
driver.find_element_by_id("medicalSupport").clear()
driver.find_element_by_id("medicalSupport").send_keys(u"测试")
driver.find_element_by_id("shoppingSupport").clear()
driver.find_element_by_id("shoppingSupport").send_keys(u"测试")
driver.find_element_by_id("lifeSupport").clear()
driver.find_element_by_id("lifeSupport").send_keys(u"测试")
driver.find_element_by_css_selector("button.ant-btn.ant-btn-primary").click()
driver.find_element_by_xpath("//button[@type='button']").click()
#driver.find_element_by_xpath("//button[@type='button']").click()
#物业类型

driver.implicitly_wait(30)
#点击新增物业
driver.find_element_by_css_selector("div.ant-row button.ant-btn.add-btn___2_Gj5.ant-btn-ghost").click()
# 物业类型
driver.find_element_by_css_selector("div.ant-select-selection__placeholder").click()
driver.find_element_by_css_selector("li.ant-select-dropdown-menu-item-active.ant-select-dropdown-menu-item").click()
driver.find_element_by_css_selector("input.ant-radio-input").click()
driver.find_element_by_xpath("(//input[@value='on'])[2]").click()
#户型均价
driver.find_element_by_id("propertyPrice").clear()
driver.find_element_by_id("propertyPrice").send_keys("12345")
sleep(2)
#建筑类型
driver.find_element_by_css_selector("input.ant-checkbox-input").click()
#物业费
driver.find_element_by_id("propertyFee").clear()
driver.find_element_by_id("propertyFee").send_keys("12")
#产权年限
driver.find_element_by_xpath("//div[6]/div[2]/div/div/div/span").click()
driver.find_element_by_xpath("//div[5]/div/div/div/ul/li[5]").click()
sleep(3)
# 装修情况!!!
driver.find_element_by_xpath("(//input[@value='on'])[13]").click()
#确认
driver.find_element_by_xpath("(//button[@type='button'])[5]").click()

# 户型

# 添加户型
driver.find_element_by_css_selector("div.add-content___XtQxn > div").click()
#户型配置
driver.find_element_by_id("flatName").clear()
driver.find_element_by_id("flatName").send_keys("12312")
# 户型结构
driver.find_element_by_xpath("//div[2]/div[2]/div[2]/div/div/div/div/div/div/div").click()
driver.find_element_by_css_selector("li.ant-select-dropdown-menu-item-active.ant-select-dropdown-menu-item").click()
#户型面积
driver.find_element_by_id("flatArea").clear()
driver.find_element_by_id("flatArea").send_keys("123")
#户型均价
driver.find_element_by_id("flatAvprice").click()
driver.find_element_by_id("flatAvprice").clear()
driver.find_element_by_id("flatAvprice").send_keys("12345")
#得房率
driver.find_element_by_id("flatRate").clear()
driver.find_element_by_id("flatRate").send_keys("12")
#装修情况
driver.find_element_by_xpath("(//input[@value='on'])[2]").click()
driver.find_element_by_xpath("(//input[@value='on'])[5]").click()
sleep(2)
#添加户型图
try:
    driver.find_element_by_css_selector("span.ant-upload > button.ant-btn.ant-btn-ghost").click()
    os.system('D:\\Python\\Shop_test\\common\\upfile.exe')
    sleep(2)
except BaseException as e:
    print(e)
#保存
driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
#滚动页面
js = "var q=document.documentElement.scrollTop=1000"
driver.execute_script(js)
sleep(3)
#保存&下一步
driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
sleep(2)
driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

# 楼盘相册

#效果图
driver.find_element_by_css_selector("i.anticon.anticon-plus").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image2.exe')
sleep(3)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image1.exe')
sleep(3)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image3.exe')
sleep(3)
driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
sleep(3)
#实景图
driver.find_element_by_xpath("//div[@id='HouseAlbumCard[102]']/div/i").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image2.exe')
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image1.exe')
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image3.exe')
sleep(1)
driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
#规划图
driver.find_element_by_xpath("//div[@id='HouseAlbumCard[103]']/div/i").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image2.exe')
sleep(1)
driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
#配套图

driver.find_element_by_xpath("//div[@id='HouseAlbumCard[105]']/div/i").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()

os.system('D:\\Python\\Shop_test\\common\\image2.exe')
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image1.exe')
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image3.exe')
sleep(1)
driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
#沙盘图
driver.find_element_by_xpath("//div[@id='HouseAlbumCard[202]']/div/i").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/div[1]/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\image2.exe')
sleep(1)
driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
# 滚动页面
js = "var q=document.documentElement.scrollTop=1000"
driver.execute_script(js)
sleep(2)
# 下一步
driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

#沙盘图

#上传图片
driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[5]/form/div[1]/div[1]/div/div/div/span/div/span/i").click()
os.system('D:\\Python\\Shop_test\\common\\shapan.exe')
sleep(5)
#添加楼栋
driver.find_element_by_link_text(u"楼栋管理").click()
driver.find_element_by_css_selector("span.ant-input-wrapper.ant-input-group > input.ant-input.ant-input-lg").clear()
driver.find_element_by_css_selector("span.ant-input-wrapper.ant-input-group > input.ant-input.ant-input-lg").send_keys(u"1栋")
driver.find_element_by_css_selector("button.ant-btn.ant-btn-sm").click()
driver.find_element_by_css_selector("button.ant-modal-close").click()
#主推楼盘
driver.find_element_by_css_selector("input.ant-checkbox-input").click()
#开盘时间
driver.find_element_by_xpath("//input[@value='']").click()
driver.find_element_by_xpath("//tr[4]/td[3]/div").click()
#入住时间
driver.find_element_by_xpath("//input[@value='']").click()
driver.find_element_by_css_selector("a.ant-calendar-next-year-btn").click()
driver.find_element_by_css_selector("td.ant-calendar-cell.ant-calendar-selected-day > div.ant-calendar-date").click()


driver.find_element_by_id("laddersNum").clear()
driver.find_element_by_id("laddersNum").send_keys("1")
driver.find_element_by_id("familyNum").clear()
driver.find_element_by_id("familyNum").send_keys("2")
driver.find_element_by_id("floorNum").clear()
driver.find_element_by_id("floorNum").send_keys("33")
# 滚动页面
js = "var q=document.documentElement.scrollTop=1000"
driver.execute_script(js)
sleep(2)
driver.find_element_by_id("unitNum").clear()
driver.find_element_by_id("unitNum").send_keys("2")
#选择户型
driver.find_element_by_css_selector("div.ant-col-24 > label.ant-checkbox-wrapper > span.ant-checkbox > input.ant-checkbox-input").click()
#选择楼栋
driver.find_element_by_xpath("//div[@id='root']/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[5]/form/div/div/div/div[2]/div/div/div").click()
driver.find_element_by_css_selector("li.ant-select-dropdown-menu-item-active.ant-select-dropdown-menu-item").click()

driver.find_element_by_css_selector("button.ant-btn.ant-btn-primary").click()
driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
#销售概况

driver.find_element_by_id("houseSaleAddress").click()
driver.find_element_by_id("houseSaleAddress").clear()
driver.find_element_by_id("houseSaleAddress").send_keys(u"深圳南山科技园")
driver.find_element_by_css_selector("button.ant-btn.ant-btn-sm").click()
driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
driver.find_element_by_id("houseSaleTelephone").clear()
driver.find_element_by_id("houseSaleTelephone").send_keys("13122233312")
driver.find_element_by_xpath("(//input[@value=''])[4]").click()
driver.find_element_by_xpath("//tr[4]/td[3]/div").click()
driver.find_element_by_xpath("(//input[@value=''])[3]").click()
driver.find_element_by_css_selector("a.ant-calendar-next-year-btn").click()
driver.find_element_by_css_selector(
    "td.ant-calendar-cell.ant-calendar-selected-day > div.ant-calendar-date").click()
driver.find_element_by_id("housePrice").clear()
driver.find_element_by_id("housePrice").send_keys("12345")
driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
#开发商

driver.find_element_by_id("houseDeveloper").clear()
driver.find_element_by_id("houseDeveloper").send_keys(u"测试")

driver.find_element_by_xpath("//div[@id='root']/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[7]/form/div[2]/div[2]/div/div/div/div").click()
driver.find_element_by_css_selector("li.ant-select-dropdown-menu-item-active.ant-select-dropdown-menu-item").click()
driver.find_element_by_id("houseInvestor").clear()
driver.find_element_by_id("houseInvestor").send_keys(u"测试")
driver.find_element_by_id("houseDeveloperIntroduction").clear()
driver.find_element_by_id("houseDeveloperIntroduction").send_keys(u"测试")
#保存
driver.find_element_by_css_selector("button.ant-btn.ant-btn-primary").click()
sleep(3)
#发布
driver.find_element_by_xpath("(//button[@type='button'])[2]").click()






