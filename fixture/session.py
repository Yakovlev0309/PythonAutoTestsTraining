

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
        return self.get_logged_user() == username

    def get_logged_user(self):
        return self.app.wd.find_element("xpath", "//div/div[1]/form/b").text[1:-1]

    def ensure_login(self, username, password):
        if self.is_logged_in(): # вход выполнен
            if self.is_logged_in_as(username): # вход выполнен под тем же именем
                return
            else: # вход выполнен под другим именем
                self.logout() # выход
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in(): # вход выполнен
            self.logout() # выход
