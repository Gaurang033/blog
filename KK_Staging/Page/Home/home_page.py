from Lib.Page import Page
from Page.Home.home_page_elements import HomePageElements

__author__ = 'Gaurang_Shah1'


class HomePage(HomePageElements, Page):

    def _validate_page(self, *args, **kwargs):
        self.wait_tool.wait_until_element_is_visible(self.logout_link)

    def get_user_name(self):
        return self.user_name_link().text
