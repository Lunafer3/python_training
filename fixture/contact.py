from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def returne_home_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='nav']/ul/li[1]/a").click()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("notes", contact.notes)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.returne_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create(self, contact):
        wd = self.app.wd
        # open add form contact
        wd.find_element_by_link_text("add new").click()
        # fill contact
        self.fill_contact(contact)
        # submit contact
        wd.find_element_by_name("submit").click()
        self.returne_home_page()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.returne_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact(new_contact_data)
        wd.find_element_by_name("update").click()
        self.returne_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.returne_home_page()

    def get_contact_list(self):
        wd = self.app.wd
        self.returne_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            firstname = element.find_element_by_css_selector("td:nth-child(3)").text
            contacts.append(Contact(id=id, firstname=firstname))
        return contacts
