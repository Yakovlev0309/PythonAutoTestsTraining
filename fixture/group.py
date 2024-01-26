

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def openGroupsPage(self):
        self.app.wd.find_element("link text", "groups").click()

    def returnToGroupsPage(self):
        self.app.wd.find_element("link text", "group page").click()

    def create(self, group):
        wd = self.app.wd
        # open groups page
        self.openGroupsPage()
        # init group creation
        wd.find_element("name", "new").click()
        # fill group form
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element("name", "submit").click()
        # return to groups page
        self.returnToGroupsPage()
    
    def deleteFirst(self):
        wd = self.app.wd
        self.openGroupsPage()
        # select first group
        wd.find_element("name", "selected[]").click()
        # submit deletion
        wd.find_element("name", "delete").click()
        # return to groups page
        self.returnToGroupsPage()

    def editFirst(self, header):
        wd = self.app.wd
        self.openGroupsPage()
        wd.find_element("name", "selected[]").click()
        wd.find_element("name", "edit").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(header)
        wd.find_element("name", "update").click()
        self.returnToGroupsPage()
