from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def openContactsForm(self):
        self.app.wd.find_element(By.LINK_TEXT, "add new").click()

    def addNewContact(self, contact):
        wd = self.app.wd
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "bday").click()
        dropdown = wd.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.birthDate.bday}']").click()
        wd.find_element(
            By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(15)"
        ).click()
        wd.find_element(By.NAME, "bmonth").click()
        dropdown = wd.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.birthDate.bmonth}']").click()
        wd.find_element(
            By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(7)"
        ).click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys(contact.birthDate.byear)
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)
        wd.find_element(By.XPATH, "(//input[@name='submit'])[2]").click()

    def returnToMainPage(self):
        self.app.wd.find_element(By.LINK_TEXT, "home page").click()

    def add(self, contact):
        self.openContactsForm()
        self.addNewContact(contact)
        self.returnToMainPage()
