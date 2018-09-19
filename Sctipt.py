# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Sctipt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://xf.fangdd.net/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sctipt(self):
        driver = self.driver
        driver.get(self.base_url + "/baishan/53059.html")
        driver.find_element_by_link_text(u"登录 / 注册").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("13122233312")
        driver.find_element_by_css_selector("span[name=\"getAuthCode\"]").click()
        driver.find_element_by_name("code").clear()
        driver.find_element_by_name("code").send_keys("111111")
        driver.find_element_by_css_selector("input.confirm").click()
        for i in range(60):
            try:
                if u"成功领取返现券\n 您可享受以下优惠：\n ¥ 9111返现券\n购买本楼盘任意户型，签约后返还现金\n有效期：2017.06.15—2018.02.01\n \n 返现券使用流程 1领取返现 2新房买家顾问带看 3售楼处签约成交 4找买家顾问申请返现 \n \n孙林鹏\n新房买家顾问\n如果您对楼盘、返现或者政策等有疑问，都可以找我。我将为您详细解答！\n致电TA" == driver.find_element_by_css_selector("div[name=\"layout\"]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if u"团购报名 关闭 \n 报名成功\n 您可享受以下团购优惠 2000抵5万 \n \n孙林鹏\n新房买家顾问\n如果您对楼盘、返现或者政策等有疑问，都可以找我。我将为您详细解答！" == driver.find_element_by_id("modalGrouponSuccess").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_name("coupon").click()
        driver.find_element_by_css_selector("#modalCouponSuccess>div.base-modal > div.header > a.modal-close").click()
        driver.find_element_by_link_text(u"立即参团").click()
        driver.find_element_by_css_selector("#modalGrouponSuccess >div.base-modal > div.header > a.modal-close").click()
        driver.find_element_by_name("freeCallBtn").click()
        driver.find_element_by_name("codeimage").click()
        driver.find_element_by_css_selector("#modalFreeCallSuccess > div.base-modal > div.header > a.modal-close").click()
    
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
