# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.LINK_TEXT, "new").click()
        # fill group form
        wd.find_element(By.LINK_TEXT, "group_name").click()
        wd.find_element(By.LINK_TEXT, "group_name").clear()
        wd.find_element(By.LINK_TEXT, "group_name").send_keys(group.name)
        wd.find_element(By.LINK_TEXT, "group_header").click()
        wd.find_element(By.LINK_TEXT, "group_header").clear()
        wd.find_element(By.LINK_TEXT, "group_header").send_keys(group.header)
        wd.find_element(By.LINK_TEXT, "group_footer").click()
        wd.find_element(By.LINK_TEXT, "group_footer").clear()
        wd.find_element(By.LINK_TEXT, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.LINK_TEXT, "submit").click()
        self.return_to_group_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.LINK_TEXT, "user").click()
        wd.find_element(By.LINK_TEXT, "user").clear()
        wd.find_element(By.LINK_TEXT, "user").send_keys(username)
        wd.find_element(By.LINK_TEXT, "pass").click()
        wd.find_element(By.LINK_TEXT, "pass").clear()
        wd.find_element(By.LINK_TEXT, "pass").send_keys(password)
        wd.find_element(By.LINK_TEXT, "//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()
