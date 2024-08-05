from time import sleep

from pages.base_page import BasePage
from pages.locators import PageRegisterLocators


class RegisterAccount(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def first_name_field(self):
        return self.find_element(PageRegisterLocators.FIRST_NAME_FIELD)

    @property
    def last_name_field(self):
        return self.find_element(PageRegisterLocators.LAST_NAME_FIELD)

    @property
    def email_field(self):
        return self.find_element(PageRegisterLocators.EMAIL_FIELD)

    @property
    def password_field(self):
        return self.find_element(PageRegisterLocators.PASSWORD_FIELD)

    @property
    def subscribe_checkbox(self):
        return self.find_element(PageRegisterLocators.SUBSCRIBE_CHECKBOX)

    @property
    def policy_checkbox(self):
        return self.find_element(PageRegisterLocators.POLICY_CHECKBOX)

    @property
    def continue_btn(self):
        return self.find_element(PageRegisterLocators.CONTINUE_BTN)

    def first_name_field_input(self, first_name):
        self.first_name_field.clear()
        return self.first_name_field.send_keys(first_name)

    def last_name_field_input(self, last_name):
        self.last_name_field.clear()
        return self.last_name_field.send_keys(last_name)

    def email_field_input(self, email):
        self.email_field.clear()
        return self.email_field.send_keys(email)

    def password_field_input(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def subscribe_checkbox_switch(self):
        self.subscribe_checkbox.click()

    def policy_checkbox_switch(self):
        self.policy_checkbox.click()

    def continue_btn_click(self, delay=0):
        self.continue_btn.click()
        sleep(delay)


















