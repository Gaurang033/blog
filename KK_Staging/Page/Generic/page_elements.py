from Lib.Page import Page

__author__ = 'Gaurang_Shah1'


class PageElements:

    login_link = lambda self: self.driver.find_element_by_link_text("Logg inn")
