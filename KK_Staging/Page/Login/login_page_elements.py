__author__ = 'Gaurang_Shah1'


class LoginPageElements:

    username_editbox = lambda self: self.driver.find_element_by_id("j_username")
    password_editbox = lambda self: self.driver.find_element_by_id("j_password")
    login_button = lambda self: self.driver.find_element_by_id("loginButton")
