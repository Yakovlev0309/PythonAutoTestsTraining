

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def logout(self):
        # FIXME без второго нажатия ничего не происходит
        logoutBtn = self.app.wd.find_element("link text", "Logout")
        logoutBtn.click()
        logoutBtn.click()

    def is_logged_in(self):
        return len(self.app.wd.find_elements("link text", "Logout")) > 0

    def is_logged_in_as(self, username):
        return self.app.wb.find_element("xpath", "//div/div[1]/form/b").text == f"({username})"

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
