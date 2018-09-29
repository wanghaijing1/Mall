# encoding: utf-8
from config import config_stage
import time
import os
import unittest
#我的发票页面
class Invoice(unittest.TestCase):
     def invoice(self):
       browser = config_stage.driver
       browser.get(config_stage.MALL_HOST)
       time.sleep(config_stage.WAIT_TIME)
       #在首页中点击:"用户中心"
       browser.find_element_by_class_name("use_center").click()
       time.sleep(config_stage.WAIT_TIME)
       #点击：“我的发票” 进入到【发的发票页面】
       browser.find_element_by_link_text(u"我的发票").click()
       time.sleep(config_stage.WAIT_TIME)
       #点击：“申请开票” 按钮
       browser.find_element_by_id("requestInvoiceBtn").click()
       time.sleep(config_stage.WAIT_TIME)
       #【增值税普通发票】
       #获取:"开票金额"的id，并且给他进行赋值
       browser.find_element_by_id("amount").send_keys("0.01")
       #获取发票类型，默认点击：“增值税普通发票”
       #browser.find_element_by_xpath("//*[@class='radio-span fl']/label")
       browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div[3]/span[2]/label[1]/input").click()
       #获取抬头类型，默认点击:"企业"
       browser.find_element_by_xpath("//*[@id='titleTypeBox']/span[2]/label[1]/input").click()
       #先清空发票抬头
       # browser.find_element_by_id("titleId").clear()
       # browser.find_element_by_class_name("add-title-btn").click()
       #给发票抬头进行赋值
       browser.find_element_by_id("companyName").send_keys(u"研发申请发票测试")
       # 获取纳税人识别号的id值，并且给他进行赋值
       browser.find_element_by_id("identifyNumberId").send_keys("1122334455667788")
       #获取证明文件的id
       browser.find_element_by_id("normalUploadFile").click()
       #并且进行上传图片
       os.system("D:\\upfile,exe")
       time.sleep(5)
       #获取发票备注的id值，并且给他进行赋值
       browser.find_element_by_id("invoiceRemark").send_keys(u"研发测试研发测试研发测试")
       #获取发票要求
       browser.find_element_by_id("applyRemark").send_keys(u"TestTest")
       #获取邮寄地址
       browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div[6]/div/div/ul/li[1]/label/input").click()
       #点击：“提交” 按钮
       browser.find_element_by_class_name("uc-submit").click()
       time.sleep(config_stage.WAIT_TIME)
       #弹出信息确认框
       browser.find_element_by_xpath("//*[@class='bounced-btn']/input").click()
       time.sleep(config_stage.WAIT_TIME)
       #点击:"确认" 按钮
       browser.find_element_by_link_text(u"确认").click()
       time.sleep(config_stage.WAIT_TIME)


       #【查看】
       #点击:"查看" 按钮
       browser.find_element_by_link_text(u"查看").click()
       time.sleep(config_stage.WAIT_TIME)
       #点击：“我知道了” 按钮
       browser.find_element_by_id("okBtn").click()
       time.sleep(config_stage.WAIT_TIME)

       #撤销
       #点击：“撤销” 按钮
       browser.find_element_by_link_text(u"撤销").click()
       #弹出：“您确定要撤销该申请吗” 点击：“确定” 按钮
       browser.find_element_by_xpath("/html/body/div[11]/div/div/div[2]/a[1]").click()
       time.sleep(config_stage.WAIT_TIME)
       #弹出：“撤销该申请成功” 点击：“确认” 按钮
       #browser.find_element_by_link_text(u"确认").click()
       browser.find_element_by_xpath("/html/body/div[11]/div/div/div[2]/a[1]").click()
       time.sleep(config_stage.WAIT_TIME)

       # #修改（修改成：增值税专用发票）
       # #点击:"修改" 按钮
       # browser.find_element_by_link_text(u"修改").click()
       # time.sleep(config_stage.WAIT_TIME)
       # #先清空开票金额
       # browser.find_element_by_id("amount").clear()
       # #获取开票金额的id，并且给他进行赋值
       # browser.find_element_by_id("amount").send_keys("2100")
       # #获取：发票内容，默认给他租赁服务费
       # browser.find_element_by_id("invoiceContentId").send_keys(u"租赁服务费")
       # #获取：“发票类型”为：“增值税专用发票”
       # browser.find_element_by_xpath("//*[@id='normalForm']/div/div[3]/span[2]/label[2]/input").click()
       # #先清空发票抬头
       # browser.find_element_by_id("companyName").clear()
       # #重新获取发票抬头公司名称，并且给他重新赋值
       # browser.find_element_by_id("companyName").send_keys(u"北京易点淘网络技术有限公司")
       # #点击：“上传所需资料”按钮，进行上传资料
       # browser.find_element_by_id("normalUploadFile").click()
       # os.system("D:\\upfile.exe")
       # #先清空纳税人识别号的信息
       # browser.find_element_by_id("taxerId").clear()
       # #给纳税人识别号进行重新赋值
       # browser.find_element_by_id("taxerId").send_keys("01122121212")
       # #先清空【工商注册地址】 的信息
       # browser.find_element_by_id("companyAddress").clear()
       # #获取【工单注册地址】的id，并且给他重新赋值
       # browser.find_element_by_id("companyAddress").send_keys(u"西二旗大街")
       # #先清空【工商注册电话】的id
       # browser.find_element_by_id("companyTel").clear()
       # #获取【工商注册电话】，并且给他重新赋值
       # browser.find_element_by_id("companyTel").send_keys("15801234112")
       # #先清空【开户行】的地址
       # browser.find_element_by_id("companyBank").clear()
       # #给开户行进行重新赋值
       # browser.find_element_by_id("companyBank").send_keys(u"建设银行")
       # #先清空【银行账户】
       # browser.find_element_by_id("companyAccount").clear()
       # #给银行账户进行重新赋值
       # browser.find_element_by_id("companyAccount").send_keys("6217000340000565980")
       # #先清空【备注】信息
       # browser.find_element_by_id("apply_remark").clear()
       # #给【备注】信息，进行重新赋值
       # browser.find_element_by_id("apply_remark").send_keys(u"修改发票")
       # #获取邮寄地址信息，默认进行点击
       # browser.find_element_by_xpath("//*[@class='invoice-button']/input").click()
       # time.sleep(config_stage.WAIT_TIME)
       # #点击：“提交” 按钮
       # browser.find_element_by_class_name("uc-bounced-button").click()
       # time.sleep(config_stage.WAIT_TIME)
       # #会弹出【发票内容】 的信息，点击：“确认” 按钮
       # browser.find_element_by_link_text(u"确认").click()
       # time.sleep(config_stage.WAIT_TIME)
       # #修改后，撤销
       # #点击【撤销】 按钮
       # browser.find_element_by_link_text(u"撤销").click()
       # #会弹出发票确认信息，点击：“确定”
       # browser.find_element_by_class_name("ok-btn").click()
       # time.sleep(config_stage.WAIT_TIME)
       # #会弹出【发票】撤销的弹出框，点击：“确认” 按钮
       # browser.find_element_by_link_text(u"确认").click()
       # time.sleep(config_stage.WAIT_TIME)



















