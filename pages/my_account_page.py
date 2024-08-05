from time import sleep

from pages.base_page import BasePage
from pages.locators import MyAccountLocators


class MyAccount(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def edit_account_item(self):
        return self.find_element(MyAccountLocators.EDIT_ACCOUNT_ITEM)

    def edit_account_item_click(self, delay=0):
        self.edit_account_item.click()
        sleep(delay)
