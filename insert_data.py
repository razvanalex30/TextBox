# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from create_driver import SeleniumLibraryExt
from robot.libraries.BuiltIn import BuiltIn
import SeleniumLibrary


class InsertData:
   
    def retrieve_text_boxes(self):
        self.driver = SeleniumLibraryExt.create_driver()
        label_dict = dict()
        xpaths = list()
        form_1 = self.driver.find_elements_by_xpath("//div[@class='col-md-9 col-sm-12']//input")
        for elem in form_1:
            key = elem.get_attribute('id')
            xpath = f"//div[@class='col-md-9 col-sm-12']//input[@id='{key}']"
            xpaths.append(xpath)
        form_2 = self.driver.find_elements_by_xpath("//div[@class='col-md-9 col-sm-12']//textarea")
        for elem in form_2:
            key = elem.get_attribute('id')
            xpath = f"//div[@class='col-md-9 col-sm-12']//textarea[@id='{key}']"
            xpaths.append(xpath)
        form_3 = self.driver.find_elements_by_xpath("//div[@class='col-md-3 col-sm-12']//label")
        for i in range(len(form_3)):
            label_dict[form_3[i].text] = xpaths[i]
        self.dict = label_dict

    def insert_data(self, dictionary):
        for key in dictionary:
            if key in self.dict:
                text_box = self.driver.find_element_by_xpath(self.dict[key])
                text_box.clear()
                text_box.send_keys(dictionary[key])
