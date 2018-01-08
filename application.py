from selenium.webdriver.firefox.webdriver import WebDriver
__author__ = 'alex'

class Application:

    def __init__(self):
        self.wd = WebDriver()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Выйти").click()
        # logout

    def vozv_group(self):
        wd = self.wd
        # submit group creation
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.wd
        # oprn group page
        wd.find_element_by_link_text("Группы").click()
        #wd.find_element_by_class_name('admin').click()
        #wd.find_element_by_css_selector("li.admin").click()
        #wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[3]/a").click()

    def sozd_groups(self, group):
        # init group creation
        wd = self.wd
        self.open_group_page()
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

    def destroy(self):
        self.wd.quit()
