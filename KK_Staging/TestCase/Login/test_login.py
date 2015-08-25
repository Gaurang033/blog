# -*- coding: utf-8 -*-

from Config import application
from Lib.test_class import TestClass
from Page.Generic.Navigate import Navigate
from Page.Login.login_page import LoginPage


__author__ = 'Gaurang_Shah1'


class TestLogin(TestClass):

    def test_login(self):
        navigate = Navigate(self.driver)
        navigate.go_to_login_page()
        login_page = LoginPage(self.driver)
        homepage = login_page.login()
        print homepage.get_user_name()
        self.assertEqual(application.user_name.decode('utf8'), homepage.get_user_name())
