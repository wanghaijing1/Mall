# encoding: utf-8
import sys
sys.path.append("./")
import unittest
import datetime
from mall.Customer import Customer
from mall.Order import Order
#from mall.Test import Test
from mall.Address import Address
from mall.Account import Account
from mall.Invoice import Invoice
from mall.OrderRelet import OrderRelet
from mall.Month import Month
from mall.ApplyDeposit import AppleDeposit
from mall.RequestRecycle import RequestRecycle
from mall.BindingPhone import BindingPhone
from mall.Mydevice import Mydevice
#from mall.Device_log import Device_Log
from mall.Device import Device
from mall.Deposit import Deposit
import os
from HTMLTestRunner import HTMLTestRunner
import ssl
import urllib.request


if __name__ == "__main__":
     default_encoding = 'utf-8'
     suiteTest = unittest.TestSuite()
     #登录
     suiteTest.addTest(Customer("login"))
     # 立即下单
     suiteTest.addTest(Order("order"))
     #订单续租页面
     suiteTest.addTest(OrderRelet("orderrelet"))
     #我的账户
     suiteTest.addTest(Account("account"))
     #我的账单
     suiteTest.addTest(Month("month"))
     #我的设备
     suiteTest.addTest(Mydevice("mydevice"))
     #设备变更记录页面
     suiteTest.addTest(Device("device"))
     #申请免押金
     #suiteTest.addTest(Deposit("deposit"))
     #我的免押金额度
     # suiteTest.addTest(AppleDeposit("appledeposit"))
     #我的发票
     suiteTest.addTest(Invoice("invoice"))
     #退换货返修
     suiteTest.addTest(RequestRecycle("requestrecycle"))
     #账户安全
     suiteTest.addTest(BindingPhone("bindingphone"))
     #快递地址
     suiteTest.addTest(Address("address"))
     now = datetime.datetime.now()
     file_name = 'D://test_case/' + now.strftime('%Y-%m-%d_%H-%M-%S') + '.html'
     fp = open(file_name, 'wb')
     runner = HTMLTestRunner(stream=fp, title='商城测试报告', description='执行情况：')
     runner.run(suiteTest)
     fp.close()


