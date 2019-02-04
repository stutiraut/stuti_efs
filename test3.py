import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Crm_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_crm(self):
           user = "instructor"
           pwd = "instructor1a"
           driver = self.driver
           driver.maximize_window()
           driver.get("http://127.0.0.1:8000/admin")
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(3)
           assert "Posted Blog Entry"
           driver.get("http://127.0.0.1:8000")
           time.sleep(1)
           # Clicks customer details
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
           time.sleep(2)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[11]/a").click()
           time.sleep(2)
