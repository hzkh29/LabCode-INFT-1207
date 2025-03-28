# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestGURU99LoginB():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_gURU99LoginB(self):
    self.driver.get("https://demo.guru99.com/test/newtours/index.php")
    self.driver.set_window_size(1133, 816)
    self.driver.find_element(By.NAME, "userName").click()
    self.driver.find_element(By.NAME, "userName").send_keys("test0089")
    self.driver.find_element(By.NAME, "password").send_keys("123456")
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Login Successfully"
  
