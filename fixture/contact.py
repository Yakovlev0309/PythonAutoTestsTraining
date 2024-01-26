

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def openContactsForm(self):
        self.app.wd.find_element("link text", "add new").click()

    def addNewContact(self, contact):
        wd = self.app.wd
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").send_keys(contact.firstname)
        wd.find_element("name", "lastname").click()
        wd.find_element("name", "lastname").send_keys(contact.lastname)
        wd.find_element("name", "nickname").click()
        wd.find_element("name", "nickname").send_keys(contact.nickname)
        wd.find_element("name", "company").click()
        wd.find_element("name", "company").send_keys(contact.company)
        wd.find_element("name", "address").click()
        wd.find_element("name", "address").send_keys(contact.address)
        wd.find_element("name", "bday").click()
        dropdown = wd.find_element("name", "bday")
        dropdown.find_element("xpath", f"//option[. = '{contact.birthDate.bday}']").click()
        wd.find_element("css selector", "select:nth-child(61) > option:nth-child(15)").click()
        wd.find_element("name", "bmonth").click()
        dropdown = wd.find_element("name", "bmonth")
        dropdown.find_element("xpath", f"//option[. = '{contact.birthDate.bmonth}']").click()
        wd.find_element("css selector", "select:nth-child(62) > option:nth-child(7)").click()
        wd.find_element("name", "byear").click()
        wd.find_element("name", "byear").send_keys(contact.birthDate.byear)
        wd.find_element("name", "theform").click()
        wd.find_element("name", "notes").click()
        wd.find_element("name", "notes").send_keys(contact.notes)
        wd.find_element("xpath", "(//input[@name='submit'])[2]").click()

    def returnToMainPage(self):
        self.app.wd.find_element("link text", "home page").click()

    def add(self, contact):
        self.openContactsForm()
        self.addNewContact(contact)
        self.returnToMainPage()

    def deleteFirst(self):
        wd = self.app.wd
        # select first contact
        wd.find_element("name", "selected[]").click()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        # accept deletion alert
        wd.switch_to.alert.accept()

    def editFirst(self, home, mobile):
        wd = self.app.wd
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        wd.find_element("name", "home").clear()
        wd.find_element("name", "home").send_keys(home)
        wd.find_element("name", "mobile").clear()
        wd.find_element("name", "mobile").send_keys(mobile)
        wd.find_element("name", "update").click()
        self.returnToMainPage()
