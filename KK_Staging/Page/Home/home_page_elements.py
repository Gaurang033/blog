__author__ = 'Gaurang_Shah1'


class HomePageElements:

    user_name_link = lambda self: self.driver.find_element_by_xpath("//a[@href='/min-side/']")
    logout_link = lambda self: self.driver.find_element_by_xpath("//a[@href='/logout']")