from selenium import webdriver


class Application:
    def __init__(self):
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

    def destroy(self):
        self.wd.quit()
