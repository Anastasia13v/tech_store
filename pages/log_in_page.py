from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def email_field(self):
        return self.find_element(LoginPageLocators.EMAIL_FIELD)

    @property
    def password_field(self):
        return self.find_element(LoginPageLocators.PASSWORD_FIELD)

    @property
    def login_btn(self):
        return self.find_element(LoginPageLocators.LOGIN_BTN)

    def email_field_input(self, email):
        self.email_field.clear()
        return self.email_field.send_keys(email)

    def password_field_input(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def login_btn_click(self):
        self.login_btn.click()

