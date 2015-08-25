import abc
import unittest2
from Lib.wait_tool import WaitTool

__author__ = 'Gaurang_Shah1'


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait_tool = WaitTool(self.driver)
        self._validate_page()

    @abc.abstractmethod
    def _validate_page(self, *args, **kwargs):
        return