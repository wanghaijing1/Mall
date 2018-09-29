# encoding: utf-8
from selenium import webdriver
import time
import unittest
from config import config_stage
#订单续租页面
class OrderRelet(unittest.TestCase):
    def orderrelet(self):
        browser = config_stage.driver
        browser.get(config_stage.MALL_HOST)
        #点击:"用户中心"，跳转到用户中心页面
        browser.find_element_by_class_name("use_center").click()
        time.sleep(config_stage.WAIT_TIME)
        #点击:"订单续租"，跳转到订单续租页面
        browser.find_element_by_link_text(u"订单续租").click()
        time.sleep(config_stage.WAIT_TIME)