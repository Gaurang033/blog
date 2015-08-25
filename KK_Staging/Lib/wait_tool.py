__author__ = 'Gaurang_Shah1'


from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitTool:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def wait_until_element_is_visible(self, method, *args):
        """
        This function will wait for element to be enable in UI
        NOTE : if you are using lamda so please send the method directly
        ex : element_to_wait = lamda self: self.findelement_by_xpath("//abcd")
        then use : wait_until_element_is_invisible(self.element_to_wait)
        no use like this : wait_until_element_is_invisible(self.element_to_wait())
        :param method: method without calling (object of method)
        :param args: if lamda is excepting any args then send here, if not then leave it blank
        """
        self.wait.until(EC.visibility_of(method(*args)), " elements still visible after 45 sec")

    def wait_until_element_is_invisible(self, method, *args):
        """
        This function will wait for element to be disable in UI
        NOTE : if you are using lamda so please send the method directly
        ex : element_to_wait = lamda self: self.findelement_by_xpath("//abcd")
        then use : wait_until_element_is_invisible(self.element_to_wait)
        no use like this : wait_until_element_is_invisible(self.element_to_wait())
        :param method: method without calling (object of method)
        :param args: if lamda is excepting any args then send here, if not then leave it blank
        """
        try:
            self.wait.until_not(EC.visibility_of(method(*args)), "element is still visible after 45 sec")
        except (NoSuchElementException, StaleElementReferenceException):
            # In the case of NoSuchElement, returns true because the element is
            # not present in DOM. The try block checks if the element is present
            # but is invisible.
            # In the case of StaleElementReference, returns true because stale
            # element reference implies that element is no longer visible.
            pass