from pages.base_page import BasePage
from pages.locators import MyAccountEditLocators


class MyAccountEdit(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def first_name_field(self):
        return self.find_element(MyAccountEditLocators.FIRST_NAME_FIELD)

    @property
    def last_name_field(self):
        return self.find_element(MyAccountEditLocators.LAST_NAME_FIELD)

    @property
    def email_field(self):
        return self.find_element(MyAccountEditLocators.EMAIL_FIELD)

    def first_name_field_read(self):
        return self.first_name_field.get_attribute("value")

    def first_name_field_input(self, first_name):
        self.first_name_field.clear()
        return self.first_name_field.send_keys(first_name)

    def last_name_field_read(self):
        return self.last_name_field.get_attribute("value")

    def last_name_field_input(self, last_name):
        self.last_name_field.clear()
        return self.last_name_field.send_keys(last_name)

    def email_field_read(self):
        return self.email_field.get_attribute("value")

    def email_field_input(self, email):
        self.email_field.clear()
        return self.email_field.send_keys(email)

