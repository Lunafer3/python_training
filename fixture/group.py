from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def returne_group_page(self):
        wd = self.app.wd
        # return group page
        wd.find_element_by_link_text("group page").click()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group(self, group):
        wd = self.app.wd
        self.type("group_name", group.gr_name)
        self.type("group_header", group.gr_header)
        self.type("group_footer", group.gr_footer)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # open add form
        wd.find_element_by_name("new").click()
        # fill group
        self.fill_group(group)
        # submit group
        wd.find_element_by_name("submit").click()
        self.returne_group_page()
        self.group_cache = None

    def edit_first_group(self):
        self.edit_group_by_index(0)

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        self.select_group_by_index(index)
        # open edit form
        wd.find_element_by_name("edit").click()
        # fill group
        self.fill_group(new_group_data)
        # update group
        wd.find_element_by_name("update").click()
        # returne group page
        self.returne_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        self.select_group_by_index(index)
        # delete group
        wd.find_element_by_name("delete").click()
        # returne group page
        self.returne_group_page()
        self.group_cache = None

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(gr_name=text, id=id))
        return list(self.group_cache)
