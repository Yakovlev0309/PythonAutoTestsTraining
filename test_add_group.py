# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)
    
    def test_add_group(self):
        dw = self.dw
        dw.get("http://localhost/addressbook/")
        dw.find_element("name", "user").click()
        dw.find_element("name", "user").clear()
        dw.find_element("name", "user").send_keys("admin")
        dw.find_element("name", "pass").clear()
        dw.find_element("name", "pass").send_keys("secret")
        dw.find_element("xpath", "//input[@value='Login']").click()
        dw.find_element("link text", "groups").click()
        dw.find_element("name", "new").click()
        dw.find_element("name", "group_name").click()
        dw.find_element("name", "group_name").clear()
        dw.find_element("name", "group_name").send_keys("qeweq")
        dw.find_element("name", "group_header").click()
        dw.find_element("name", "group_header").click()
        dw.find_element("name", "group_header").clear()
        dw.find_element("name", "group_header").send_keys("dfhsdfg")
        dw.find_element("name", "group_footer").click()
        dw.find_element("name", "group_footer").clear()
        dw.find_element("name", "group_footer").send_keys("fdfdgf")
        dw.find_element("name", "submit").click()
        dw.find_element("link text", "group page").click()
        dw.find_element("link text", "Logout").click()
    
    def is_element_present(self, how, what):
        try: self.dw.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.dw.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.dw.quit()

if __name__ == "__main__":
    unittest.main()
