#coding=utf-8

"""
调用方法如下：

WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)

 这里需要特别注意的是until或until_not中的可执行方法method参数，很多人传入了WebElement对象，这是不正确的。在这里，
 你可以用selenium提供的 expected_conditions 模块中的各种条件，也可以用WebElement的 is_displayed() 、
 is_enabled()、is_selected() 方法，或者用自己封装的方法都可以
"""
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os, sys

class myclass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://console.huaweicloud.com/vpc/?region=cn-north-1&locale=en-us#/vpc/vpcmanager/dashboard")
        self.driver.maximize_window()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("userNameId"))
        #WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.ID, "btn_submit"))
        self.driver.find_element_by_id("userNameId").clear()
        self.driver.find_element_by_id("userNameId").send_keys("gwx613100")
        self.driver.find_element_by_id("pwdId").send_keys("Bigdata_2013")
        time.sleep(2)
        self.driver.find_element_by_id("btn_submit").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_dashborad_vpc(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_vpc"))
        self.driver.find_element_by_id("_vpc").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        # self.driver.find_element_by_link_text("Basic Information")
        print('********test_dashborad_vpc*****pass***')

    def test_dashboard_sg(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_securityGroup"))
        self.driver.find_element_by_id("_securityGroup").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_sg*************pass*********')

    def test_dashboard_acls(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_firewall"))
        self.driver.find_element_by_id("_firewall").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_acls************pass*********')

    def test_dashboard_eips(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_eip"))
        self.driver.find_element_by_id("_eip").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_eip*************pass*********')

    def test_dashboard_shareBandwidth(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_shareBandwidth"))
        self.driver.find_element_by_id("_shareBandwidth").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_shareBandwidth*************pass*********')

    def test_dashboard_nat(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_nat"))
        self.driver.find_element_by_id("_nat").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_nat*************pass*********')

    def test_dashboard_elb(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_elb"))
        self.driver.find_element_by_id("_elb").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btn_createEnhanceELB"))
        self.driver.find_element_by_id("btn_createEnhanceELB").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_elb*************pass*********')

    def test_dashboard_peering(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_peering"))
        self.driver.find_element_by_id("_peering").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_peering*************pass*********')

    def test_dashboard_vpngw(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_vpngw"))
        self.driver.find_element_by_id("_vpngw").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_vpngw*************pass*********')

    def test_dashboard_vpn(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_vpn"))
        self.driver.find_element_by_id("_vpn").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_vpn*************pass*********')

    def test_dashboard_dline(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_dline"))
        self.driver.find_element_by_id("_dline").click()
        time.sleep(3)
        self.driver.find_element_by_id("vpc_vpcmanager_physicalDlineTe").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btns1"))
        self.driver.find_element_by_id("btns1").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_dline*************pass*********')

    def test_dashboard_crossNetwork(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("_crossNetwork"))
        self.driver.find_element_by_id("_crossNetwork").click()
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("btn_buy"))
        self.driver.find_element_by_id("btn_buy").click()
        time.sleep(3)
        #self.driver.find_element_by_link_text("Basic Information")
        print('**************test_dashboard_crossNetwork*************pass*********')

    # def test_dashboard_vpcep(self):
    #     WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_class("icon-cloud-service-extend-vpc-endpoint"))
    #     self.driver.find_element_by_class_name("icon-cloud-service-extend-vpc-endpoint").click()
    #     time.sleep(3)
    #     WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_class("ti-btn-large"))
    #     self.driver.find_element_by_class_name("ti-btn-large").click()
    #     time.sleep(3)
    #     self.driver.find_element_by_link_text("Basic Information")
    #     print('**************test_dashboard_vpcep*************pass*********')ERROR
if __name__=='__main__':

    unittest.main()