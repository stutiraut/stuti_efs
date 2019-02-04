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
           elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a").click()
            #add new customer
           time.sleep(3)
           elem = driver.find_element_by_id("id_name")
           elem.send_keys("stuti")
           elem = driver.find_element_by_id("id_address")
           elem.send_keys("Uno")

           elem = driver.find_element_by_id("id_cust_number")
           elem.send_keys("1")

           elem = driver.find_element_by_id("id_city")
           elem.send_keys("Omaha")

           elem = driver.find_element_by_id("id_state")
           elem.send_keys("NE")

           elem = driver.find_element_by_id("id_zipcode")
           elem.send_keys("68106")

           elem = driver.find_element_by_id("id_email")
           elem.send_keys("sraut@unomaha.edu")

           elem = driver.find_element_by_id("id_cell_phone")
           elem.send_keys("1234888695")
           elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()

           time.sleep(5)
           assert "Posted Blog Entry"
           driver.get("http://127.0.0.1:8000")
           time.sleep(1)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
           time.sleep(2)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[9]/a").click()
           time.sleep(5)
           elem = driver.find_element_by_id("id_address")
           #edits the address
           elem.send_keys("Crosswinds1")
           time.sleep(2)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
           time.sleep(2)
           #deletes the customer
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[9]/td[10]/a").click()
           time.sleep(2)



