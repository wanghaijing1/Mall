#encoding: utf-8
from selenium import webdriver
import time
import unittest
from config import config_stage
#设备变更记录页面
class Device(unittest.TestCase):
    def device(self):
        browser = config_stage.driver
        browser.get(config_stage.MALL_HOST)
        #点击:"用户中心"，跳转到用户中心页面
        browser.find_element_by_class_name("use_center").click()
        time.sleep(config_stage.WAIT_TIME)
        browser.find_element_by_link_text(u"设备变更记录").click()
        time.sleep(config_stage.WAIT_TIME)