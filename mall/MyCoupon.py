# encoding: utf-8
from selenium import webdriver
import time
import unittest
from config import config_stage
#我的优惠劵页面
class MyCoupon(unittest.TestCase):
    def mycoupon(self):
        browser = config_stage.driver
        browser.get(config_stage.MALL_HOST)
        #跳转到用户中心页面
        browser.find_element_by_class_name("use_center").click()
        time.sleep(config_stage.WAIT_TIME)
        #点击：“我的优惠劵”，跳转到【我的优惠劵】页面
        browser.find_element_by_xpath("/html/body/div[2]/div/ul/li[2]/ul/li[6]/a").click()
        time.sleep(config_stage.WAIT_TIME)