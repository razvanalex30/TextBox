# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from create_driver import SeleniumLibraryExt
from robot.libraries.BuiltIn import BuiltIn
import SeleniumLibrary


class InsertData:

    def insert_full_name(self, full_name=None):
        self.driver = SeleniumLibraryExt.create_driver()
        text_box = self.driver.find_element_by_id("userName")
        text_box.clear()
        text_box.send_keys(full_name)

    def insert_email(self, email=None):
        # self.driver = SeleniumLibraryExt.create_driver()
        text_box = self.driver.find_element_by_id("userEmail")
        text_box.clear()
        text_box.send_keys(email)

    def insert_current_address(self, current_address=None):
        # self.driver = SeleniumLibraryExt.create_driver()
        text_box = self.driver.find_element_by_id("currentAddress")
        text_box.clear()
        text_box.send_keys(current_address)

    def insert_permanent_address(self, permanent_address=None):
        # self.driver = SeleniumLibraryExt.create_driver()
        text_box = self.driver.find_element_by_id("permanentAddress")
        text_box.clear()
        text_box.send_keys(permanent_address)
