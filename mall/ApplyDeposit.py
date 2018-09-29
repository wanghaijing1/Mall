# encoding: utf-8
from selenium import webdriver
import time
import unittest
from config import config_stage
#我的免押金额度页面
class AppleDeposit(unittest.TestCase):
    def appledeposit(self):
        browser = config_stage.driver
        browser.get(config_stage.MALL_HOST)
        #进入到用户中心页面
        browser.find_element_by_class_name("use_center").click()
        time.sleep(config_stage.WAIT_TIME)
        #跳转到 我的免押金额度 页面
        browser.find_element_by_link_text(u"我的免押金额度").click()
        time.sleep(config_stage.WAIT_TIME)
        js = "$('html,body').animate({scrollTop: '10000px'}, 7000)"
        browser.execute_script(js)