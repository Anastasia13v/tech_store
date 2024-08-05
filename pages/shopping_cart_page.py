from pages.base_page import BasePage
from pages.locators import ShoppingCartLocators


class ShoppingCart (BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def checkout_btn(self):
        return self.find_element(ShoppingCartLocators.CHECKOUT_BTN)

    def checkout_btn_click(self):
        self.checkout_btn.click()