from create_driver import SeleniumLibraryExt
from robot.libraries.BuiltIn import BuiltIn
import SeleniumLibrary

class VerifyData:

    

    # def find_output(self):
    #     output = self.driver.find_element_by_xpath("//*[@id='output']/div")
    #     output_elements = output.find_element_by_tag_name("p")

    def find_name(self):
        self.driver = SeleniumLibraryExt.create_driver()
        output_name = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='name']")
        name = output_name.text
        if name != "":
            print("Name was found!")

    def find_email(self):
        self.driver = SeleniumLibraryExt.create_driver()
        output_email = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='email']")
        email = output_email.text
        if email != "":
            print("Email was found!")

    def find_current_address(self):
        self.driver = SeleniumLibraryExt.create_driver()
        output_current_address = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='currentAddress']")
        current_address = output_current_address.text
        if current_address != "":
            print("Current Address was found!")

    def find_permanent_address(self):
        self.driver = SeleniumLibraryExt.create_driver()
        output_permanent_address = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='permanentAddress']")
        permanent_address = output_permanent_address.text
        if permanent_address != "":
            print("Permanent Address was found!")
