# coding=utf-8
from selenium import webdriver
import unittest
import time
import HTMLTestRunner  # 引入 HTMLTestRunner 包
import os


class Baidu(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []

    # 百度搜索用例
    def test_baidu_search(self):
        u'''百度搜索用例'''
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get("http://www.baidu.com/")
        self.driver.implicitly_wait(10)
        driver.find_element_by_id("kw").send_keys("HTNMLTestRunner")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "Html_report":
    # 定义个报告存放路径
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    #os.mkdir('D:\\Python_script\\report')
    filename = 'D:\\Python_script\\report\\' + now + 'result.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='用例执行情况：')
        # 测试套件
        testunit = unittest.TestSuite()
        # 添加测试用例到测试套件中
        testunit.addTest(Baidu("test_baidu_search"))
    # 运行测试用例
        runner.run(testunit)
    # 关闭报告文件
        fp.close()
