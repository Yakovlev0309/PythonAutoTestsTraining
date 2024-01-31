from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements("name", "new")) > 0):
            wd.find_element("link text", "groups").click()

    def return_to_groups_page(self):
        self.app.wd.find_element("link text", "group page").click()

    def change_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(value)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        # open groups page
        self.open_groups_page()
        # init group creation
        wd.find_element("name", "new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element("name", "submit").click()
        # return to groups page
        self.return_to_groups_page()

    def select_first_group(self):
        self.app.wd.find_element("name", "selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element("name", "delete").click()
        # return to groups page
        self.return_to_groups_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element("name", "edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element("name", "update").click()
        self.return_to_groups_page()

    def count(self):
        self.open_groups_page()
        return len(self.app.wd.find_elements("name", "selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for element in wd.find_elements("css selector", "span.group"):
            text = element.text
            id = element.find_element("name", "selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups
