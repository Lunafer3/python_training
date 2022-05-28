class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//input[@value='Enter']").click()
        self.return_to_home_page()


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("contact_firstname", contact.firstname)
        self.change_field_value("contact_middlename", contact.middlename)
        self.change_field_value("contact_lastname", contact.lastname)
        self.change_field_value("contact_homephone", contact.homephone)
        self.change_field_value("contact_homephone2", contact.homephone2)
        self.change_field_value("contact_mobile", contact.mobile)
        self.change_field_value("contact_workphone", contact.workphone)
        self.change_field_value("contact_faxphone", contact.faxphone)
        self.change_field_value("contact_mail", contact.mail)
        self.change_field_value("contact_mail2", contact.mail2)
        self.change_field_value("contact_mail3", contact.mail3)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if not text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select first contact
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']")[index].click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # fill contacts form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("https://localhost/addressbook/")