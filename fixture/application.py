from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.chrome.options import Options


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            options = Options()
            options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            self.wd = webdriver.Chrome(options=options)
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        
        # helpers initialization
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
