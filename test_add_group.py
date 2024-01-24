# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def openHomePage(self):
        self.wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.wd.find_element("name", "user").click()
        self.wd.find_element("name", "user").clear()
        self.wd.find_element("name", "user").send_keys(username)
        self.wd.find_element("name", "pass").clear()
        self.wd.find_element("name", "pass").send_keys(password)
        self.wd.find_element("xpath", "//input[@value='Login']").click()

    def openGroupsPage(self):
        self.wd.find_element("link text", "groups").click()

    def createGroup(self, group):
        # init group creation
        self.wd.find_element("name", "new").click()
        # fill group form
        self.wd.find_element("name", "group_name").click()
        self.wd.find_element("name", "group_name").clear()
        self.wd.find_element("name", "group_name").send_keys(group.name)
        self.wd.find_element("name", "group_header").click()
        self.wd.find_element("name", "group_header").click()
        self.wd.find_element("name", "group_header").clear()
        self.wd.find_element("name", "group_header").send_keys(group.header)
        self.wd.find_element("name", "group_footer").click()
        self.wd.find_element("name", "group_footer").clear()
        self.wd.find_element("name", "group_footer").send_keys(group.footer)
        # submit group creation
        self.wd.find_element("name", "submit").click()

    def returnToGroupsPage(self):
        self.wd.find_element("link text", "group page").click()

    def logout(self):
        self.wd.find_element("link text", "Logout").click()

    def test_add_group(self):
        self.openHomePage()
        self.login(username="admin", password="secret")
        self.openGroupsPage()
        self.createGroup(Group(name="test group", header="test header", footer="test footer"))
        self.returnToGroupsPage()        
        self.logout()
        
    def test_add_empty_group(self):
        self.openHomePage()
        self.login(username="admin", password="secret")
        self.openGroupsPage()
        self.createGroup(Group(name="", header="", footer=""))
        self.returnToGroupsPage()        
        self.logout()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
