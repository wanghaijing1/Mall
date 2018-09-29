#encoding: utf-8
from config import config_stage
import time
import unittest
from selenium.webdriver.support.ui import Select
#快递地址页面
class Address(unittest.TestCase):
     def address(self):
         browser = config_stage.driver
         browser.get(config_stage.MALL_HOST)
         browser.find_element_by_class_name("use_center").click()
         time.sleep(config_stage.WAIT_TIME)
         browser.find_element_by_link_text(u"快递地址").click()
         time.sleep(config_stage.WAIT_TIME)
         #新增快递地址
         browser.find_element_by_id("contacterName").send_keys(u"王海静")
         browser.find_element_by_id("provinceId").send_keys(u"北京")
         time.sleep(config_stage.WAIT_TIME)
         browser.find_element_by_id("bcityId").send_keys(u"北京市")
         time.sleep(config_stage.WAIT_TIME)
         browser.find_element_by_id("scityId").send_keys(u"海淀区")
         time.sleep(config_stage.WAIT_TIME)
         browser.find_element_by_id("address").send_keys(u"北京市海淀区西二旗大街")
         browser.find_element_by_id("phone").send_keys("15810651004")
         browser.find_element_by_class_name("submit-btn").click()
         time.sleep(config_stage.WAIT_TIME)
         browser.find_element_by_link_text(u"确认").click()
         #设为默认地址
         # browser.find_elements_by_link_text(u"设为默认地址").click()
         #修改地址
         browser.find_element_by_link_text(u"修改").click()
         time.sleep(config_stage.WAIT_TIME)
         browser.find_element_by_id("mContacterName").clear()
         browser.find_element_by_id("mContacterName").send_keys(u"研发测试")
         Select(browser.find_element_by_id("mProvinceId")).select_by_index(1)
         Select(browser.find_element_by_id("mBCityId")).select_by_index(1)
         Select(browser.find_element_by_id("mSCityId")).select_by_index(1)
         time.sleep(config_stage.WAIT_TIME)
         browser.find_element_by_id("mAddress").clear()
         browser.find_element_by_id("mAddress").send_keys(u"啦啦啦***********")
         browser.find_element_by_id("mPhone").clear()
         browser.find_element_by_id("mPhone").send_keys("15820181755")
         browser.find_element_by_xpath("/html/body/div[11]/div/div/div/div[2]/a[1]").click()
         time.sleep(3)
         browser.find_element_by_xpath("/html/body/div[12]/div/div/div[2]/a").click()
         time.sleep(config_stage.WAIT_TIME)
         #删除地址
         browser.find_element_by_link_text(u"删除").click()
         browser.find_element_by_link_text(u"确认").click()
         time.sleep(3)
         browser.find_element_by_class_name("ok-btn").click()



