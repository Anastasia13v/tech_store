from pages.base_page import BasePage
from pages.locators import OrdersLocators


class OrdersPage (BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def status_pending(self):
        return self.find_element(OrdersLocators.STATUS_PENDING)

    def status_pending_read(self):
        return self.status_pending.text
