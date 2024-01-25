from selenium import webdriver
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def openHomePage(self):
        self.wd.get("http://localhost/addressbook/")

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

    def destroy(self):
        self.wd.quit()
