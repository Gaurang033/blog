from Lib.Page import Page
from Lib.wait_tool import WaitTool
from Page.Generic.page_elements import PageElements

__author__ = 'Gaurang_Shah1'


class Navigate(PageElements, Page):

    # def __init__(self, driver):
    #     self.driver = driver
    #     self.wait_tool = WaitTool(self.driver)

    def _validate_page(self, *args, **kwargs):
        pass

    def go_to_login_page(self):
        self.login_link().click()
        self.wait_tool.wait_until_element_is_invisible(self.login_link)
