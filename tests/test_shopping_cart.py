from pages.checkout_page import CheckoutPage
from pages.checkout_success_page import CheckoutSuccess
from pages.home_page import HomePage
from pages.orders_page import OrdersPage
from pages.register_account_page import RegisterAccount
from pages.shopping_cart_page import ShoppingCart


def test_buy_products(driver, user_randomizer):
    first_name = user_randomizer.build_random_user_first_name()
    last_name = user_randomizer.build_random_user_last_name()
    email = user_randomizer.build_random_email_name()
    password = "1234567"

    main_page = HomePage(driver)
    main_page.navigate_to_home_page()
    main_page.open_register_page()

    register_account_page = RegisterAccount(driver)
    register_account_page.first_name_field_input(first_name)
    register_account_page.last_name_field_input(last_name)
    register_account_page.email_field_input(email)
    register_account_page.password_field_input(password)
    register_account_page.subscribe_checkbox_switch()
    register_account_page.policy_checkbox_switch()
    register_account_page.continue_btn_click(3)

    main_page.navigate_to_home_page()
    main_page.scroll_to_featured(5)
    main_page.featured_one_add_to_cart()
    main_page.featured_two_add_to_cart()
    main_page.scroll_up(5)
    main_page.proceed_to_shopping_cart(5)

    shopping_cart_page = ShoppingCart(driver)
    shopping_cart_page.scroll_down()
    shopping_cart_page.checkout_btn_click()

    checkout_page = CheckoutPage(driver)
    checkout_page.shipping_first_name_field_input(first_name)
    checkout_page.shipping_last_name_field_input(last_name)
    checkout_page.shipping_address_field_input("Test address")
    checkout_page.shipping_city_field_input("Test city")
    checkout_page.shipping_country_dropdown_select_by_value("220")
    checkout_page.shipping_post_code_field_input("02102")
    checkout_page.shipping_region_dropdown_select_by_value("3490")
    checkout_page.shipping_continue_btn_click()

    checkout_page.shipping_method_choose_btn_click(3)
    checkout_page.shipping_flat_rate_radio_btn_select(3)
    checkout_page.shipping_method_continue_btn_click(3)

    checkout_page.payment_method_choose_btn_click()
    checkout_page.payment_method_cash_radio_btn_select()
    checkout_page.payment_method_continue_btn_click()

    checkout_page.scroll_down()
    checkout_page.confirm_order_btn_click(7)

    checkout_success = CheckoutSuccess(driver)
    checkout_success.my_account_click(3)
    checkout_success.order_history_item_click(3)

    orders_page = OrdersPage(driver)
    actual_result_status = orders_page.status_pending_read()
    assert actual_result_status == "Pending"



