# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random
from time import sleep


class test1():
    def test_untitled_test_case(self, sum=0, left=0):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://licai.fangdd.com"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_css_selector("div.btn > a.btn-log").click()
        driver.find_element_by_id("mobile").clear()
        driver.find_element_by_id("mobile").send_keys("13058019302")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("11111a")
        driver.find_element_by_id("signin").click()
        sleep(2)
        driver.find_element_by_id("biaoCountDown0").click()
        driver.find_element_by_id("money").clear()
        if left != 0:
            money = left
        else:
            money = random.randint(80, 200) * 100
        print(money)
        driver.find_element_by_id("money").send_keys(money)
        driver.find_element_by_id("agree").click()
        driver.find_element_by_css_selector("button.btn").click()
        driver.find_element_by_id("payWords").clear()
        driver.find_element_by_id("payWords").send_keys("900211")
        driver.find_element_by_id("payBtn").click()
        driver.quit()
        return money
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    test2 = test1()
    s = 252880
    while (s > 5000):
        result = test2.test_untitled_test_case(s, 0)
        s = s - result
    test2.test_untitled_test_case(0, s)

