from create_driver import SeleniumLibraryExt
from robot.libraries.BuiltIn import BuiltIn
import SeleniumLibrary

class VerifyData:

    def check_data(self):
        self.driver = SeleniumLibraryExt.create_driver()
        form_1 = self.driver.find_elements_by_xpath("//div[@class='border col-md-12 col-sm-12']/p")
        for elem in form_1:
            field = elem.get_attribute('id')
            xpath = self.driver.find_element_by_xpath(f"//div[@class='border col-md-12 col-sm-12']/p[@id='{field}']")
            header = xpath.text
            labels = header.split(":")
            print(f"{labels[0]} was completed!")
        
        
    # def find_name(self):
        # self.driver = SeleniumLibraryExt.create_driver()
        # output_name = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='name']")
        # name = output_name.text
        # if name != "":
            # print("Name was found!")
            #
    # def find_email(self):
        # self.driver = SeleniumLibraryExt.create_driver()
        # output_email = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='email']")
        # email = output_email.text
        # if email != "":
            # print("Email was found!")
            #
    # def find_current_address(self):
        # self.driver = SeleniumLibraryExt.create_driver()
        # output_current_address = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='currentAddress']")
        # current_address = output_current_address.text
        # if current_address != "":
            # print("Current Address was found!")
            #
    # def find_permanent_address(self):
        # self.driver = SeleniumLibraryExt.create_driver()
        # output_permanent_address = self.driver.find_element_by_xpath("//*[@id='output']/div//p[@id='permanentAddress']")
        # permanent_address = output_permanent_address.text
        # if permanent_address != "":
            # print("Permanent Address was found!")
