# encoding: utf-8
#import urllib2
import base64
from io import BytesIO

from config import config_stage
from PIL import Image
import pytesseract
import unittest
import time
import urllib.request
import re
from selenium import webdriver
#import A as B 指的是给予A库一个B的别称，帮助记忆
import check_captcha as cc


import selenium
dir(selenium)
print(dir(selenium))
#登录页面（存在两种方法）
class Customer(unittest.TestCase):
     def login(self):
         browser = config_stage.driver
         browser.get(config_stage.MALL_HOST)
         assert u"易点租" in browser.title
         #把窗体最大化
         browser.maximize_window()

         #点击：“登录” 按钮
         browser.find_element_by_class_name("login").click()
         time.sleep(3)
         #获取：“用户名”，并给他进行赋值
         browser.find_element_by_id("phone").send_keys(config_stage.MALL_USER)
         #获取：“密码”，并给他进行赋值
         browser.find_element_by_id("password").send_keys(config_stage.MALL_PASSWD)
         jsessionid = browser.get_cookie("JSESSIONID")['value']
         #识别验证码(第一种方法)

         # browser.find_element_by_id("codeImage")
         # rand_number_url = browser.find_element_by_id("codeImage").get_attribute("src")
         # opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
         # opener.addheaders.append(('Cookie', 'JSESSIONID='+jsessionid))
         # request = urllib.request.Request(rand_number_url)
         # picture = opener.open(request).read()
         # local = open('f:/tmp.png', 'wb')
         # local.write(picture)
         # local.close()
         # img = Image.open("f:/tmp.png")
         # code = pytesseract.image_to_string(img).replace(" ","")
         # code = re.sub("\D", "", code)
         # browser.find_element_by_id("imgCode").send_keys(code)
         # browser.find_element_by_id("submitBtn").click()
         # time.sleep(config_stage.WAIT_TIME)


         # #实现滚动条的功能
         # js = "$('html,body').animate({scrollTop: '10000px'}, 7000)"
         # browser.execute_script(js)

         #获取验证码第二种方法（通过坐标轴获取+API 识别图片验证码）
         codeImageWebEle = browser.find_element_by_id('codeImage')
         location = codeImageWebEle.location
         size = codeImageWebEle.size
         left = location['x']
         top = location['y']
         right = location['x'] + size['width']
         bottom = location['y'] + size['height']
         # 截取全屏保存
         name = 'f:/temp.png'
         browser.save_screenshot(name);
         fullImg = Image.open(name)
         im = fullImg.crop((left, top, right, bottom))
         im.save(name)
         image = None
         #把图片转换成base64位
         with open(name, "rb") as f:
             image = base64.b64encode(f.read())
         #通过API识别验证码，详细步骤如下
         code = cc.check_captcha_img(image)
         print(code)
         code = re.sub("\D", "", code)
         browser.find_element_by_id("imgCode").send_keys(code)
         browser.find_element_by_id("submitBtn").click()
         time.sleep(config_stage.WAIT_TIME)



         #直接获取cookien方法
         # driver = webdriver.Firefox()
         # host = "https://stage-www.edianzu.cn"
         # driver.maximize_window()
         # driver.get(host)
         # driver.add_cookie({'name': 'token', 'value': '869c359a92f1bf00a19023ceb6fb477e'})
         # driver.get(host)











