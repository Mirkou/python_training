# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False



class tre(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        #self.wd.implicitly_wait(60)
    
    def test_1(self):
        success = True
        wd = self.wd
        wd.get("https://family.disney.com/")
        wd.find_element_by_link_text("Crafts").click()
        self.assertTrue(success)
    
#    def tearDown(self):
#        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
