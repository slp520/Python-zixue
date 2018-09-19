# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep

class ddd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://passport.fangdd.net"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True
    
    def test_ddd(self):
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get(self.base_url + "/passport/authorize.do?client_id=dddai&response_type=code&redirect_uri=http://10.0.6.58:8017/ddd-manage/oauth2Login")
        driver.find_element_by_id("tu").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("sunlinpeng")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("xmn900211!")
        driver.find_element_by_id("smscode").clear()
        driver.find_element_by_id("smscode").send_keys("123456")
        driver.find_element_by_id("login").click()
        driver.find_element_by_xpath("//ul[@id='nav-list']/li[2]/a/span").click()
        driver.find_element_by_link_text(u"待处理报备单").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | content_iframe | ]]
        # driver.find_element_by_xpath("/html/body/div[1]/div/section/div/form-grid/div/div/div[1]/h1/span/a/span").click()
        # driver.find_element_by_link_text(u"深圳").click()
        sleep(5)
        # driver.find_element_by_class_name('caret').click()
        # sleep(2)
        # driver.find_element_by_link_text(u"新增报备单").click()
        # sleep(2)
        driver.find_element_by_css_selector("li.active > a.dropdown-toggle > span.menu-text").click()
        driver.find_element_by_link_text(u"待处理订单").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | content_iframe | ]]
        driver.find_element_by_xpath(u"//input[@value='放款初审']").click()
        sleep(2)
        driver.find_element_by_xpath(u"//input[@value='下一步']").click()
        driver.find_element_by_name("loanProvider").click()
        sleep(1)
        driver.find_element_by_css_selector("label.radio-inline").click()
        sleep(1)
        driver.find_element_by_css_selector("div.loan-block.active > span.ng-binding").click()
        driver.find_element_by_xpath("(//input[@name='prodcut'])[4]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").send_keys("6")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_name("expectAmount").clear()
        driver.find_element_by_name("expectAmount").send_keys("301")
        Select(driver.find_element_by_xpath("//select[@id='']")).select_by_visible_text(u"月")
        driver.find_element_by_css_selector("option[value=\"number:2\"]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("1000")
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("100")
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("1000")
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("10")
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("//label[3]").click()
        driver.find_element_by_name("repaymentFrom").click()
        driver.find_element_by_xpath("//div[2]/label[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(u"测试第二批")
        driver.find_element_by_xpath("//input[@type='tel']").clear()
        driver.find_element_by_xpath("//input[@type='tel']").send_keys("13111122211")
        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(u"测试的奥")
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("//label[4]/span").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("(//button[@type='button '])[2]").click()
        driver.find_element_by_name("bankAccountCityName").clear()
        driver.find_element_by_name("bankAccountCityName").send_keys(u"深圳")
        driver.find_element_by_name("bankAccountNumber").clear()
        driver.find_element_by_name("bankAccountNumber").send_keys("6214856551133890")
        Select(driver.find_element_by_name("bankId")).select_by_visible_text(u"招商银行")
        driver.find_element_by_css_selector("option[value=\"number:7\"]").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("13122233321")
        driver.find_element_by_name("bankAccountName").clear()
        driver.find_element_by_name("bankAccountName").send_keys(u"测试")
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        driver.find_element_by_name("idCardNum").clear()
        driver.find_element_by_name("idCardNum").send_keys("411303198908095118")
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("(//option[@value='number:2'])[5]").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(u"测试")
        Select(driver.find_element_by_name("gender")).select_by_visible_text(u"男")
        driver.find_element_by_css_selector("select[name=\"gender\"] > option[value=\"number:1\"]").click()
        Select(driver.find_element_by_name("household")).select_by_visible_text(u"本地")
        driver.find_element_by_css_selector("select[name=\"household\"] > option[value=\"number:0\"]").click()
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("(//option[@value='number:1'])[7]").click()
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("(//option[@value='number:1'])[9]").click()
        driver.find_element_by_name("companyAddress").clear()
        driver.find_element_by_name("companyAddress").send_keys(u"测试的")
        driver.find_element_by_name("companyContact").clear()
        driver.find_element_by_name("companyContact").send_keys("13122233345")
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("(//option[@value='number:5'])[5]").click()
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("(//option[@value='number:2'])[9]").click()
        driver.find_element_by_name("monthlyIncome").clear()
        driver.find_element_by_name("monthlyIncome").send_keys("123456")
        driver.find_element_by_name("isOwner").click()
        driver.find_element_by_xpath("//button[@type='submit ']").click()
        driver.find_element_by_xpath("//button[@type='submit ']").click()
        driver.find_element_by_xpath("//button[@type='submit ']").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"对对对")
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_css_selector("option[value=\"number:2\"]").click()
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("(//option[@value='number:2'])[2]").click()
        driver.find_element_by_name("userMobileNo").clear()
        driver.find_element_by_name("userMobileNo").send_keys("13222233312")
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("//button[@type='submit ']").click()
        driver.find_element_by_xpath("//button[@type='submit ']").click()
        driver.find_element_by_css_selector("i.glyphicon.glyphicon-folder-open").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_css_selector("div.uploadBtn.state-ready").click()
        driver.find_element_by_css_selector("div.modal-footer.ng-scope > button.btn.mybutton").click()
        driver.find_element_by_css_selector("i.glyphicon.glyphicon-folder-open").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_css_selector("div.uploadBtn.state-ready").click()
        driver.find_element_by_css_selector("div.modal-footer.ng-scope > button.btn.mybutton").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//form-grid[@id='order-all-list']/div/div/div[3]/table/tbody/tr/td[12]/button").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_css_selector("form[name=\"ordermodalFrom\"] > div.modal-footer > button.btn.mybutton").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_css_selector("form[name=\"ordermodalFrom\"] > div.modal-footer > button.btn.mybutton").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
