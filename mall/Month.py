# encoding: utf-8
from selenium import webdriver
from config import  config_stage
import time
import unittest
#我的账单页面
class Month(unittest.TestCase):
    def month(self):
        browser = config_stage.driver
        browser.get(config_stage.MALL_HOST)
        #点击：“用户中心”
        browser.find_element_by_class_name("use_center").click()
        time.sleep(config_stage.WAIT_TIME)
        #进入到【我的账单】的页面
        browser.find_element_by_link_text(u"我的账单").click()
        time.sleep(10)
        js = "$('html,body').animate({scrollTop: '10000px'}, 7000)"
        browser.execute_script(js)