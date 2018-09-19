# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunner

class Login(unittest.TestCase):
    def setUp(driver):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        base_url = "http://xf.fangdd.net"
        driver.verificationErrors = []
        driver.accept_next_alert = True
    
    def test_login(driver):
        driver.get(driver.base_url + "/baishan")
        driver.find_element_by_link_text(u"登录 / 注册").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("13122233312")
        driver.find_element_by_css_selector("span[name=\"getAuthCode\"]").click()
        driver.find_element_by_name("code").clear()
        driver.find_element_by_name("code").send_keys("111111")
        driver.find_element_by_css_selector("input.confirm").click()
        driver.find_element_by_link_text(u"退出").click()
    
    def is_element_present(driver, how, what):
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(driver):
        try:
            driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(driver):
        try:
            alert = driver.switch_to_alert()
            alert_text = alert.text
            if driver.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: driver.accept_next_alert = True

    def tearDown(driver):
        driver.quit()
        driver.assertEqual([], driver.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    filename = 'D:\\test_object\\report\\result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'web站测试报告',
        description=u'用例执行情况：'
    )
    runner.run(unittest)
    fp.close()