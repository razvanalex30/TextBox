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
        
        
    
