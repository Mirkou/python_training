class GroupHelper:

    def __init__(self, app):
        self.app = app

    def vozv_group(self):
        wd = self.app.wd
        # submit group creation
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.aap.wd
        # oprn group page
        wd.find_element_by_link_text("Группы").click()
        #wd.find_element_by_class_name('admin').click()
        #wd.find_element_by_css_selector("li.admin").click()
        #wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[3]/a").click()

    def create(self, group):
        # init group creation
        wd = self.app.wd
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