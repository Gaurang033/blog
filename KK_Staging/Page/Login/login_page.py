from Lib.Page import Page
from Lib.wait_tool import WaitTool
from Page.Home.home_page import HomePage
from Page.Login.login_page_elements import LoginPageElements
from Config import application
__author__ = 'Gaurang_Shah1'


class LoginPage(LoginPageElements, Page):

    # def __init__(self, driver):
    #     self.driver = driver
    #     self.wait_tool = WaitTool(self.driver)

    def _validate_page(self, *args, **kwargs):
        pass

    def login(self):
        self.username_editbox().send_keys(application.email)
        self.password_editbox().send_keys(application.password)
        self.login_button().click()

        self.wait_tool.wait_until_element_is_invisible(self.username_editbox)

        return HomePage(self.driver)