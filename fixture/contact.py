from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_contact_form(self):
        wd = self.app.wd
        self.return_to_main_page()
        wd.find_element("link text", "add new").click()

    def change_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(value)

    def change_dropdown_value(self, dropdown_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element("name", dropdown_name).click()
            dropdown = wd.find_element("name", dropdown_name)
            dropdown.find_element("xpath", f"//option[. = '{value}']").click()
            wd.find_element("css selector", "select:nth-child(61) > option:nth-child(15)").click()

    def change_birth_date(self, birth_date):
        if birth_date is not None:
            self.change_dropdown_value("bday", birth_date.bday)
            self.change_dropdown_value("bmonth", birth_date.bmonth)
            self.change_field_value("byear", birth_date.byear)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_birth_date(contact.birth_date)
        self.change_field_value("notes", contact.notes)

    def add_new_contact(self, contact):
        self.fill_contact_form(contact)
        self.app.wd.find_element("xpath", "(//input[@name='submit'])[2]").click()

    def return_to_main_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements("id", "search_count")) > 0):
            wd.find_element("link text", "home").click()

    def add(self, contact):
        self.open_add_contact_form()
        self.add_new_contact(contact)
        self.return_to_main_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact
        wd.find_elements("name", "selected[]")[index].click()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        # accept deletion alert
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        wd.find_elements("xpath", "//img[@title='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element("name", "update").click()
        self.return_to_main_page()
        self.contact_cache = None

    def count(self):
        self.return_to_main_page()
        return len(self.app.wd.find_elements("name", "selected[]"))
    
    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_main_page()
            self.contact_cache = []
            maintable = wd.find_element("id", "maintable")
            entries = maintable.find_elements("name", "entry")
            for i in range(len(entries)):
                id = entries[i].find_element("name", "selected[]").get_attribute("value")
                tmp = entries[i].find_elements("css selector", "td")
                lastname = tmp[1].text
                firstname = tmp[2].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)
