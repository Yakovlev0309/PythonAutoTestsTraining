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
        self.group_cache = None

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        self.app.wd.find_elements("name", "selected[]")[index].click()

    def test_delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element("name", "delete").click()
        # return to groups page
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element("name", "edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element("name", "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, new_group_data):   
        self.modify_group_by_index(0, new_group_data)

    def count(self):
        self.open_groups_page()
        return len(self.app.wd.find_elements("name", "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements("css selector", "span.group"):
                text = element.text
                id = element.find_element("name", "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))  
        return list(self.group_cache)
