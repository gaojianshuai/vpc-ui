#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest

driver = webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
driver.get('https://www.126.com')
driver.maximize_window()
driver.set_window_size(1366, 768)
WebDriverWait(20, 5, 1).until(EC.presence_of_all_elements_located(By.ID, 'idInput'))
driver.find_element_by_id('idInput').send_keys('51testing')
driver.find_element_by_id('pwdInput').send_keys('123456789')
driver.find_element_by_id('loginBtn').click()
driver.quit()
wait = WebDriverWait(driver, 10)

