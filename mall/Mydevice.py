# encoding: utf-8
from selenium import webdriver
import time
import unittest
from config import config_stage
#我的设备页面
class Mydevice(unittest.TestCase):
    def mydevice(self):
        browser = config_stage.driver
        browser.get(config_stage.MALL_HOST)
        #点击:"用户中心"，跳转到用户中心页面
        browser.find_element_by_class_name("use_center").click()
        time.sleep(config_stage.WAIT_TIME)
        #进入（我的设备）页面
        browser.find_element_by_link_text(u"我的设备").click()
        time.sleep(config_stage.WAIT_TIME)
        js = "$('html,body').animate({scrollTop: '10000px'}, 7000)"
        browser.execute_script(js)