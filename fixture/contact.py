from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_contact_form(self):
        wd = self.app.wd
        self.open_home_page()
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
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_birth_date(contact.birth_date)
        self.change_field_value("notes", contact.notes)

    def add_new_contact(self, contact):
        self.fill_contact_form(contact)
        self.app.wd.find_element("xpath", "(//input[@name='submit'])[2]").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements("id", "search_count")) > 0):
            wd.find_element("link text", "home").click()

    def add(self, contact):
        self.open_add_contact_form()
        self.add_new_contact(contact)
        self.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_elements("name", "selected[]")[index].click()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        # accept deletion alert
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def open_contact_edit_by_index(self, index):
        self.open_home_page()
        self.app.wd.find_elements("xpath", "//img[@title='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        self.open_home_page()
        self.app.wd.find_elements("xpath", "//img[@title='Details']")[index].click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.open_contact_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element("name", "update").click()
        self.open_home_page()
        self.contact_cache = None

    def count(self):
        self.open_home_page()
        return len(self.app.wd.find_elements("name", "selected[]"))
    
    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements("name", "entry"):
                cells = row.find_elements("tag name", "td")
                id = cells[0].find_element("tag name", "input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)
    
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        id = wd.find_element("name", "id").get_attribute("value")
        firstname = wd.find_element("name", "firstname").get_attribute("value")
        middlename = wd.find_element("name", "middlename").get_attribute("value")
        lastname = wd.find_element("name", "lastname").get_attribute("value")
        nickname = wd.find_element("name", "nickname").get_attribute("value")
        company = wd.find_element("name", "company").get_attribute("value")
        address = wd.find_element("name", "address").get_attribute("value")
        homephone = wd.find_element("name", "home").get_attribute("value")
        mobilephone = wd.find_element("name", "mobile").get_attribute("value")
        workphone = wd.find_element("name", "work").get_attribute("value")
        secondaryphone = wd.find_element("name", "phone2").get_attribute("value")
        # birth_date = wd.find_element("name", "").get_attribute("value") # TODO доделать
        notes = wd.find_element("name", "notes").get_attribute("value")
        return Contact(id=id, firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, 
                       company=company, address=address, homephone=homephone, mobilephone=mobilephone, 
                       workphone=workphone, secondaryphone=secondaryphone, notes=notes)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        content = wd.find_element("id", "content")
        names = content.find_element("tag name", "b")
        if names is not None:
            all_names = names.text
        else:
            all_names = None
        data = content.text
        homephone = re.search("H: (.*)", data)
        mobilephone = re.search("M: (.*)", data)
        workphone = re.search("W: (.*)", data)
        secondaryphone = re.search("P: (.*)", data)
        if homephone is not None:
            homephone = homephone.group(1)
        if mobilephone is not None:
            mobilephone = mobilephone.group(1)
        if workphone is not None:
            workphone = workphone.group(1)
        if secondaryphone is not None:
            secondaryphone = secondaryphone.group(1)
        return Contact(all_names_from_view_page=all_names, 
                       homephone=homephone, mobilephone=mobilephone, 
                       workphone=workphone, secondaryphone=secondaryphone)
