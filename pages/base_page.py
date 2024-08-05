from time import sleep

from pages.locators import BasePageLocators
from pages.page import Page


class BasePage(Page):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def my_account(self):
        return self.find_element(BasePageLocators.MY_ACCOUNT_DROPDOWN)

    @property
    def register(self):
        return self.find_element(BasePageLocators.REGISTER_ITEM)

    @property
    def logout(self):
        return self.find_element(BasePageLocators.LOGOUT_ITEM)

    @property
    def login(self):
        return self.find_element(BasePageLocators.LOGIN_ITEM)

    @property
    def shopping_cart(self):
        return self.find_element(BasePageLocators.SHOPPING_CART)

    @property
    def order_history_item(self):
        return self.find_element(BasePageLocators.ORDER_HISTORY)

    @property
    def my_account_item(self):
        return self.find_element(BasePageLocators.MY_ACCOUNT_ITEM)

    def my_account_click(self, delay=0):
        self.my_account.click()
        sleep(delay)

    def register_click(self):
        self.register.click()

    def logout_click(self):
        self.logout.click()

    def login_click(self):
        self.login.click()

    def open_register_page(self):
        self.my_account_click()
        self.register_click()

    def proceed_to_shopping_cart(self, delay=0):
        self.shopping_cart.click()
        sleep(delay)

    def order_history_item_click(self, delay=0):
        self.order_history_item.click()
        sleep(delay)

    def my_account_item_click(self):
        self.my_account_item.click()

