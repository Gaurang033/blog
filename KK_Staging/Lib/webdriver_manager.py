from selenium import webdriver
from Config.webdriver import *

__author__ = 'Gaurang_Shah1'


class WebDriverManager:

    def get_driver(self):

        if browser == "firefox":
            self.driver = webdriver.Firefox()

        return self.driver


