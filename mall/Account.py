#encoding: utf-8
from config import config_stage
import unittest
import time
#我的账户页面
class Account(unittest.TestCase):
     def account(self):
         browser = config_stage.driver
         browser.get(config_stage.MALL_HOST)
         #点击首页的【用户中心】
         browser.find_element_by_class_name("use_center").click()
         time.sleep(config_stage.WAIT_TIME)
         #在用户中心中点击:"我的账户"
         browser.find_element_by_link_text(u"我的账户").click()
         time.sleep(config_stage.WAIT_TIME)
         # #充值
         #在我的账户页面中点击："充值" 按钮
         # browser.find_element_by_xpath("/html/body/div[3]/div/div/div/table[1]/tbody/tr[1]/td/div/a[1]/span").click()
         browser.find_element_by_link_text(u"充值").click()
         time.sleep(config_stage.WAIT_TIME)
         #进入到充值的页面， 获取充值文本框的id，并且给它赋值为0.01
         browser.find_element_by_id("price").send_keys("0.01")
         time.sleep(config_stage.WAIT_TIME)
         #在充值页面中， 点击:"充值" 按钮
         browser.find_element_by_class_name("trage").click()
         #页面跳转
         time.sleep(config_stage.WAIT_TIME)
         if "支付宝" not in browser.title:
             #随机定义变量：all_handles,所有窗口，目的是：加载浏览器中所有的窗口
             all_handles = browser.window_handles
             #随机定义变量:search_windows 当前窗口，目的是：获取当前的窗口
             search_windows = browser.current_window_handle
             #遍历所有的窗口
             for handle in all_handles:
                 #如果，当前打开的窗口不等于当前窗口
                 if handle != search_windows:
                     #就直接跳转到当前窗口
                     browser.switch_to_window(handle)
                     #直接进行关闭
                     browser.close()
                     #把当前窗口赋值给当前的浏览器
                     browser.switch_to_window(search_windows)
             time.sleep(config_stage.WAIT_TIME)
             #关闭当前窗口时，会弹出一个弹出框，点击：“充值成功” 按钮
             browser.find_element_by_class_name("_charge_success_btn").click()
             time.sleep(config_stage.WAIT_TIME)
             #点击，我的账户页面，跳转到当前账户的首页
             browser.find_element_by_link_text(u"我的账户").click()
             time.sleep(config_stage.WAIT_TIME)
         #提现
         #点击:"提现" 按钮
         browser.find_element_by_xpath("/html/body/div[5]/div/div/div/table[1]/tbody/tr[1]/td/div/a[2]/span").click()
         time.sleep(config_stage.WAIT_TIME)
         #获取提现中文本框的值，并给赋值为1
         browser.find_element_by_id("amount").send_keys("0.01")
         #点击：“提现申请” 按钮
         browser.find_element_by_id("submit").click()
         time.sleep(config_stage.WAIT_TIME)
         #会弹出提现文本框，点击：“确认” 按钮
         browser.find_element_by_link_text(u"确认").click()
         time.sleep(4)
         browser.refresh()
         #取消提现（点击：取消按钮）
         time.sleep(config_stage.WAIT_TIME)
         browser.find_element_by_name("cancel").click()
         time.sleep(config_stage.WAIT_TIME)
         #会弹出取消提现文本框，点击：“确认” 按钮
         browser.find_element_by_link_text(u"确认").click()
         time.sleep(config_stage.WAIT_TIME)





