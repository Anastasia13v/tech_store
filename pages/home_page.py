from time import sleep

from pages.base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = "http://localhost:80"

    def navigate_to_home_page(self):
        super().navigate_to(self.url)

    @property
    def featured_one(self):
        return self.find_element(HomePageLocators.FEATURED_ONE)

    @property
    def featured_two(self):
        return self.find_element(HomePageLocators.FEATURED_TWO)

    @property
    def h3(self):
        return self.find_element(HomePageLocators.H3)

    def featured_one_add_to_cart(self):
        self.featured_one.click()

    def featured_two_add_to_cart(self, delay=0):
        self.featured_two.click()
        sleep(delay)

    def scroll_to_featured(self, delay=0):
        self.scroll_to_element(self.h3)
        sleep(delay)

    def scroll_to_featured_with_delay(self, delay):
        self.scroll_to_element(self.h3)
        sleep(delay)





