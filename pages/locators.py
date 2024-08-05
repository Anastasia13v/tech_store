from selenium.webdriver.common.by import By


class BasePageLocators:
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//div[@class='nav float-end']/ul[@class='list-inline']/li[@class='list-inline-item']/div[@class='dropdown']/a")
    REGISTER_ITEM = (By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[1]/a")
    LOGOUT_ITEM = (By.XPATH, "//div[@class='list-group mb-3']//a[text()='Logout']")
    LOGIN_ITEM = (By.XPATH, "//*[@id='column-right']/div/a[1]")
    SHOPPING_CART = (By.XPATH, "//*[@id='top']/div/div[2]/ul/li[4]/a/span")
    ORDER_HISTORY = (By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[2]/a")
    MY_ACCOUNT_ITEM = (By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[1]/a")


class PageRegisterLocators:
    FIRST_NAME_FIELD = (By.ID, "input-firstname")
    LAST_NAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    SUBSCRIBE_CHECKBOX = (By.ID, "input-newsletter")
    POLICY_CHECKBOX = (By.XPATH, "//*[@id='form-register']/div/div/input")
    CONTINUE_BTN = (By.XPATH, "//*[@id='form-register']/div/button")


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BTN = (By.XPATH, "//*[@id='form-login']/div[3]/button")


class MyAccountLocators:
    EDIT_ACCOUNT_ITEM = (By.XPATH, "//*[@id='content']/ul[1]/li[1]/a")


class MyAccountEditLocators:
    FIRST_NAME_FIELD = (By.ID, "input-firstname")
    LAST_NAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")


class HomePageLocators:
    FEATURED_ONE = (By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > form > div > button:nth-child(1)")
    FEATURED_TWO = (By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1)")
    H3 = (By.TAG_NAME, "h3")


class ShoppingCartLocators:
    CHECKOUT_BTN = (By.XPATH, "//*[@id='content']/div[3]/div[2]/a")


class CheckoutLocators:
    SHIPPING_FIRST_NAME_FIELD = (By.ID, "input-shipping-firstname")
    SHIPPING_LAST_NAME_FIELD = (By.ID, "input-shipping-lastname")
    SHIPPING_ADDRESS_FIELD = (By.ID, "input-shipping-address-1")
    SHIPPING_CITY_FIELD = (By.ID, "input-shipping-city")
    SHIPPING_COUNTRY_DROPDOWN = (By.NAME, "country_id")
    SHIPPING_POST_CODE_FIELD = (By.ID, "input-shipping-postcode")
    SHIPPING_REGION_DROPDOWN = (By.ID, "input-shipping-zone")
    SHIPPING_CONTINUE_BTN = (By.ID, "button-shipping-address")
    SHIPPING_METHOD_CHOOSE_BTN = (By.ID, "button-shipping-methods")
    SHIPPING_FLAT_RATE_RADIO_BTN = (By.ID, "input-shipping-method-flat-flat")
    SHIPPING_METHOD_CONTINUE_BTN = (By.ID, "button-shipping-method")
    PAYMENT_METHOD_CHOOSE_BTN = (By.ID, "button-payment-methods")
    PAYMENT_METHOD_CASH_RADIO_BTN = (By.ID, "input-payment-method-cod-cod")
    PAYMENT_METHOD_CONTINUE_BTN = (By.ID, "button-payment-method")
    CONFIRM_ORDER_BTN = (By.ID, "button-confirm")


class OrdersLocators:
    STATUS_PENDING = (By.XPATH, "//*[@id='content']/div[1]/table/tbody/tr[1]/td[4]")



















