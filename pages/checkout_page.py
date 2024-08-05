from time import sleep

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import CheckoutLocators


class CheckoutPage (BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def shipping_first_name_field(self):
        return self.find_element(CheckoutLocators.SHIPPING_FIRST_NAME_FIELD)

    @property
    def shipping_last_name_field(self):
        return self.find_element(CheckoutLocators.SHIPPING_LAST_NAME_FIELD)

    @property
    def shipping_address_field(self):
        return self.find_element(CheckoutLocators.SHIPPING_ADDRESS_FIELD)

    @property
    def shipping_city_field(self):
        return self.find_element(CheckoutLocators.SHIPPING_CITY_FIELD)

    @property
    def shipping_country_dropdown(self):
        return self.find_element(CheckoutLocators.SHIPPING_COUNTRY_DROPDOWN)

    @property
    def shipping_post_code_field(self):
        return self.find_element(CheckoutLocators.SHIPPING_POST_CODE_FIELD)

    @property
    def shipping_region_dropdown(self):
        return self.find_element(CheckoutLocators.SHIPPING_REGION_DROPDOWN)

    @property
    def shipping_continue_btn(self):
        return self.find_element(CheckoutLocators.SHIPPING_CONTINUE_BTN)

    @property
    def shipping_method_choose_btn(self):
        return self.find_element(CheckoutLocators.SHIPPING_METHOD_CHOOSE_BTN)

    @property
    def shipping_flat_rate_radio_btn(self):
        return self.find_element(CheckoutLocators.SHIPPING_FLAT_RATE_RADIO_BTN)

    @property
    def shipping_method_continue_btn(self):
        return self.find_element(CheckoutLocators.SHIPPING_METHOD_CONTINUE_BTN)

    @property
    def payment_method_choose_btn(self):
        return self.find_element(CheckoutLocators.PAYMENT_METHOD_CHOOSE_BTN)

    @property
    def payment_method_cash_radio_btn(self):
        return self.find_element(CheckoutLocators.PAYMENT_METHOD_CASH_RADIO_BTN)

    @property
    def payment_method_continue_btn(self):
        return self.find_element(CheckoutLocators.PAYMENT_METHOD_CONTINUE_BTN)

    @property
    def confirm_order_btn(self):
        return self.find_element(CheckoutLocators.CONFIRM_ORDER_BTN)

    def shipping_first_name_field_input(self, first_name):
        self.shipping_first_name_field.clear()
        self.shipping_first_name_field.send_keys(first_name)

    def shipping_last_name_field_input(self, last_name):
        self.shipping_last_name_field.clear()
        self.shipping_last_name_field.send_keys(last_name)

    def shipping_address_field_input(self, address):
        self.shipping_address_field.clear()
        self.shipping_address_field.send_keys(address)

    def shipping_city_field_input(self, city):
        self.shipping_city_field.clear()
        self.shipping_city_field.send_keys(city)

    def shipping_country_dropdown_select_by_value(self, value):
        Select(self.shipping_country_dropdown).select_by_value(value)

    def shipping_post_code_field_input(self, post_code):
        self.shipping_post_code_field.clear()
        self.shipping_post_code_field.send_keys(post_code)

    def shipping_region_dropdown_select_by_value(self, value):
        Select(self.shipping_region_dropdown).select_by_value(value)

    def shipping_continue_btn_click(self):
        self.shipping_continue_btn.click()

    def shipping_method_choose_btn_click(self, delay=0):
        self.shipping_method_choose_btn.click()
        sleep(delay)

    def shipping_flat_rate_radio_btn_select(self, delay=0):
        self.shipping_flat_rate_radio_btn.click()
        sleep(delay)

    def shipping_method_continue_btn_click(self, delay=0):
        self.shipping_method_continue_btn.click()
        sleep(delay)

    def payment_method_choose_btn_click(self):
        self.payment_method_choose_btn.click()

    def payment_method_cash_radio_btn_select(self):
        self.payment_method_cash_radio_btn.click()

    def payment_method_continue_btn_click(self):
        self.payment_method_continue_btn.click()

    def confirm_order_btn_click(self, delay=0):
        self.confirm_order_btn.click()
        sleep(delay)







