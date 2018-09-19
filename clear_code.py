# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, sys,importlib
from PIL import Image,ImageEnhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

class Ypt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://shop.fangdd.net/login.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_streen(self):
        driver = self.driver
        driver.save_screenshot("D:\\aa.png")  # 截取当前网页，该网页有我们需要的验证码
        imgelement = driver.find_element_by_id("refresh-code") # 定位验证码
        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = Image.open("D:\\aa.png")  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save('D:\\frame4.png')
        img = Image.open("D:\\frame4.png")
        imgry=img.convert('L')
        sharpness=ImageEnhance.Contrast(imgry)
        sharp_img=sharpness.enhance(3.0)
        sharp_img.save("D:\\frame.tiff")
        img2 = Image.open("D:\\frame.tiff")
        # print (img2.load())
        aa = pytesseract.image_to_string(img2)

        SecretCode = input('please enter the code: ')

        print(u"识别的验证码为：")
        print(aa)
        if aa == ""or aa.isalpha()==False:  # 如果识别为空，则再一次识别
            driver.find_element_by_id("refresh-code").click()
            self.test_streen()
        return aa
    # def tearDown(self):
    #     # self.driver.quit()
if __name__=='__main__':
    unittest.main()