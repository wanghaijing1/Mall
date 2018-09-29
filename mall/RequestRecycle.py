# encoding: utf-8
from  selenium import  webdriver
from config import config_stage
import time
import unittest
#退换货返修
class RequestRecycle(unittest.TestCase):
    def requestrecycle(self):
        browser = config_stage.driver
        browser.get(config_stage.MALL_HOST)
        #点击："用户中心"，跳转到用户中心页面
        browser.find_element_by_class_name("use_center").click()
        time.sleep(config_stage.WAIT_TIME)
        #点击:"退换货返修"，跳转到:"退换货返修" 页面
        browser.find_element_by_link_text(u"退换货返修").click()
        time.sleep(config_stage.WAIT_TIME)