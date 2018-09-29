# encoding:utf-8
from config import config_stage
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#我的订单页面
class Order(unittest.TestCase):
    def order(self):
         browser = config_stage.driver
         browser.get(config_stage.MALL_HOST)
         #---------------------------------------立即下单-----------------------------------
         browser.find_element_by_xpath("//*[@id='floor-1']/div/a[2]").click()
         #定义所有变量all_handles,目的是加载所有窗口
         all_handles = browser.window_handles
         #定义当前窗口，目的是获取当前窗口111111
         search_windows = browser.current_window_handle
         #进行for循环，遍历所有的窗口
         for handle in all_handles:
              #如果当当前加载的页面不等于当前窗口
             if handle !=search_windows:
                  #获取最新的窗口
                 browser.switch_to_window(handle)
         time.sleep(config_stage.WAIT_TIME)
         #点击:"立即下单" 的按钮
         browser.find_element_by_class_name("submit-btn").click()
         time.sleep(config_stage.WAIT_TIME)
         #支付方式选择：货到付款
         #browser.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/label/input").click()
         #勾选租赁服务协议
         browser.find_element_by_class_name("select-agree").click()
         #点击："提交订单" 按钮
         browser.find_element_by_class_name("available-btn").click()
         time.sleep(config_stage.WAIT_TIME)
         #鼠标悬浮(鼠标悬浮在用户中心)
         above = browser.find_element_by_xpath("//*[@id='header-list']/li[3]/a")
         ActionChains(browser).move_to_element(above).perform()
         #通过鼠标悬浮，点击用户中心
         browser.find_element_by_xpath("//*[@id='header-list']/li[3]/ul/li[1]/a").click()
         time.sleep(3)
         #点击取消订单按钮
         browser.find_element_by_xpath("//*[@id='dataTable']/div[1]/dl/dd/a[2]").click()
         time.sleep(3)
         #点击：“确认取消订单”按钮
         browser.find_element_by_xpath("/html/body/div[11]/div/div/div[2]/a[1]").click()
         time.sleep(5)

         #点击：“确认”
         browser.find_element_by_xpath("/html/body/div[11]/div/div/div[2]/a").click()

         #在线支付
         # browser.find_element_by_xpath("/html/body/div[4]/form/div[3]/input[2]").click()
         # time.sleep(config_stage.WAIT_TIME)
         # browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/a").click()
         # time.sleep(config_stage.WAIT_TIME)
         # browser.find_element_by_xpath("/html/body/div[4]/div/ul/li[1]/ul/li[1]/a").click()
         # time.sleep(config_stage.WAIT_TIME)
         #测试
         js = "$('html,body').animate({scrollTop: '10000px'}, 7000)"
         browser.execute_script(js)
         # #--------------------------------------------测试[加入购物车]--------------------------------------
         # #自定义的变量 home，其中current_window_handle获取当前的页面的句柄
         # home = browser.current_window_handle
         # #点击商品进入到商品详情页面（商品id=100245）
         # browser.find_element_by_class_name("part-2").click()
         # #查询所有句柄信息
         # all_handles = browser.window_handles
         # #进行for循环遍历，查看所有句柄信息
         # for handle in all_handles:
         #      #如果当前的句柄不等于第一个句柄的值
         #      if handle != home:
         #           # 直接获取当前页面的句柄信息
         #           browser.switch_to_window(handle)
         # #选择意外保
         # browser.find_element_by_id("accidentService").click()
         # #选择：硬件无忧上门（鼠标悬浮的效果），自定义变量：SiteService（鼠标悬浮在【硬件无忧上门】文本框上）
         # SiteService = browser.find_element_by_id("onSiteService")
         # ActionChains(browser).move_to_element(SiteService).perform()
         # #点击：“10元的硬件无忧上门”，并进行点击
         # # browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/dl[2]/dd/div[1]/span/ul/li[2]/span[2]/span[1]").click()
         # #选择数量
         # browser.find_element_by_id("addCount").click()
         # #点击：“加入购物车” 按钮
         # browser.find_element_by_class_name("add-to-cart-btn").click()
         # time.sleep(config_stage.WAIT_TIME)
         # #点击:"去购物侧结算" 按钮
         # browser.find_element_by_link_text(u"去购物车结算").click()
         # time.sleep(config_stage.WAIT_TIME)
         # #点击：“去结算” 按钮
         # browser.find_element_by_class_name("settle-accounts").click()
         # time.sleep(config_stage.WAIT_TIME)
         # #勾选【易点租电脑设备租赁协议】
         # browser.find_element_by_class_name("select-agree").click()
         # #进行提交订单
         # browser.find_element_by_class_name("available-btn").click()
         # time.sleep(config_stage.WAIT_TIME)
         # #进行支付
         # browser.find_element_by_xpath("/html/body/div[3]/form/div[3]/input[2]").click()
         # time.sleep(config_stage.WAIT_TIME)