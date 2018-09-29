#encoding: utf-8
from config import config_stage
import time
import os
import unittest
from selenium.webdriver.common.action_chains import ActionChains
#申请免押金额度页面
class Deposit(unittest.TestCase):
    def deposit(self):
        browser = config_stage.driver
        browser.get(config_stage.MALL_HOST)
        time.sleep(config_stage.WAIT_TIME)
        #--------------------------进入到申请免押金额度页面————————————————————————
        #在首页中点击："用户中心"
        browser.find_element_by_class_name("use_center").click()
        time.sleep(config_stage.WAIT_TIME)
        #点击:"申请免押金额度"页面
        browser.find_element_by_link_text(u"我的免押金额度").click()
        time.sleep(config_stage.WAIT_TIME)
        # #点击:"申请资料" 按钮
        # browser.find_element_by_class_name("immediately-apply").click()
        # time.sleep(config_stage.WAIT_TIME)
        # #获取公司名称的id，并且给它赋值
        # browser.find_element_by_id("companyName").send_keys(u"北京易点淘网络技术有限公司研发测试")
        # #获取注册号，并且给它赋值
        # browser.find_element_by_id("companyRegistration").send_keys("1122334455667788")
        # #获取营业执照的id，进行上传图片
        # browser.find_element_by_xpath("//*[@id='businessLicense']").click()
        # os.system("E:\Test.exe")
        # #获取省，并且给它赋值
        # browser.find_element_by_id("companyProvince").send_keys(u"北京")
        # #获取市，并且给它进行赋值
        # browser.find_element_by_id("companyCity").send_keys(u"北京市")
        # #获取区，并且给它进行赋值
        # browser.find_element_by_id("companyArea").send_keys(u"海淀区")
        # #获取具体地址， 并且给它进行赋值
        # browser.find_element_by_id("companyAddress").send_keys(u"西二旗高科大厦")
        # #点击：“下一步”
        # browser.find_element_by_class_name("step-next").click()
        # time.sleep(config_stage.WAIT_TIME)
        # #获取姓名地址，并且给它进行赋值
        # browser.find_element_by_id("shareholderName").send_keys(u"王海静")
        # #获取身份证号，并且给它进行赋值
        # browser.find_element_by_id("shareholderIDCard").send_keys("110226198501272116")
        # #获取身份证正面
        # browser.find_element_by_xpath("//*[@id='idCardImage1Btn']").click()
        # os.system("E:\Test.exe")
        # #获取身份证反面
        # browser.find_element_by_xpath("//*[@id='idCardImage2Btn']").click()
        # os.system("E:\Test.exe")
        # #获取手机号，并进行给他进行赋值
        # browser.find_element_by_id("shareholderMobile").send_keys("15810651002")
        # #获取备用手机号，并给他进行赋值
        # browser.find_element_by_id("concat1Moblie").send_keys("15810651003")
        # #点击:"下一步" 并且给他进行提交
        # browser.find_element_by_id("shareholderSubmitBtn").click()
        # time.sleep(config_stage.WAIT_TIME)
        #---------------------------------点击："补充信息"---------------------------------
        #点击：“补充信息” 页面。进入到补充信息页面
        browser.find_element_by_class_name("_supplement_link").click()
        time.sleep(config_stage.WAIT_TIME)
        employees = browser.current_window_handle
        # 进入【员工社保缴纳记录】，点击：“立即完善”按钮
        browser.find_element_by_xpath("//*[@id='amountForm']/div/div[2]/table/tbody/tr[1]/td[2]/a").click()
        all_handles = browser.window_handles
        for handle in  all_handles:
             if handle !=employees:
                 browser.switch_to_window(handle)
        #上传员工图片信息
        browser.find_element_by_id("uploadFileBtn").click()
        os.system("E:\Test.exe")
        #鼠标悬浮在【证明文件】
        Employee = browser.find_element_by_class_name("show-img")
        ActionChains(browser).move_to_element(Employee).perform()
        #填写备注信息
        browser.find_element_by_class_name("_remark").send_keys(u"自动化测试员工社保缴存记录")
        #点击：“提交” 按钮
        browser.find_element_by_class_name("submitSupplementaryInfo").click()
        #---------------------【银行了流水明细】----------------------------------
        browser.find_element_by_link_text(u"我的免押金额度").click()
        browser.find_element_by_class_name("_supplement_link").click()
        time.sleep(config_stage.WAIT_TIME)
        bank = browser.current_window_handle
        browser.find_element_by_xpath("//*[@id='amountForm']/div/div[2]/table/tbody/tr[2]/td[2]/a").click()
        all_handles = browser.window_handles
        for handle in all_handles:
            if handle !=bank:
                browser.switch_to_window(handle)
        browser.find_element_by_id("uploadFileBtn").click()
        os.system("E:\Test.exe")
        browser.find_element_by_class_name("_remark").send_keys(u"自动化测试")
        browser.find_element_by_class_name("submitSupplementaryInfo").click()










