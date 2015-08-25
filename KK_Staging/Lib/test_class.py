from unittest2.case import TestCase
from Lib.wait_tool import WaitTool
from Lib.webdriver_manager import WebDriverManager
from Config.application import *

__author__ = 'Gaurang_Shah1'


class TestClass(TestCase):

    def setUp(self):
        webdriver_manager = WebDriverManager()
        self.driver = webdriver_manager.get_driver()
        self.driver.get(site_url)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()