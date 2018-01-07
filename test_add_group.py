# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        #self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def test_add_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_group_page(wd)
        self.sozd_groups(wd, Group(name="fcgdfgdfg", header="sdfsfsdfs", footer="dfgdfgdfgdfg"))
        self.vozv_group(wd)
        self.logout(wd)

    def test_add__empty_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_group_page(wd)
        self.sozd_groups(wd, Group(name="", header="", footer=""))
        self.vozv_group(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Выйти").click()
        # logout

    def vozv_group(self, wd):
        # submit group creation
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self, wd):
        # oprn group page
        wd.find_element_by_link_text("Группы").click()

    def sozd_groups(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()



    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
