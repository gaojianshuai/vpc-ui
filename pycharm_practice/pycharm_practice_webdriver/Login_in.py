#coding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
"""
调用方法如下：

WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)

 这里需要特别注意的是until或until_not中的可执行方法method参数，很多人传入了WebElement对象，这是不正确的。在这里，
 你可以用selenium提供的 expected_conditions 模块中的各种条件，也可以用WebElement的 is_displayed() 、
 is_enabled()、is_selected() 方法，或者用自己封装的方法都可以
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os, sys


def Login(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://console.huaweicloud.com/vpc/?region=cn-north-1&locale=en-us#/vpc/vpcmanager/dashboard")
    self.driver.maximize_window()
    time.sleep(3)
    WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id("userNameId"))
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.ID, "btn_submit"))
    self.driver.find_element_by_id("userNameId").clear()
    self.driver.find_element_by_id("userNameId").send_keys("gwx613100")
    self.driver.find_element_by_id("pwdId").send_keys("Bigdata_2013")
    time.sleep(2)
    self.driver.find_element_by_id("btn_submit").click()
    time.sleep(5)

