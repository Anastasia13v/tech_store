from pages.home_page import HomePage
from pages.my_account_edit_page import MyAccountEdit
from pages.my_account_page import MyAccount
from pages.register_account_page import RegisterAccount


def test_update_user_data(driver, user_randomizer):
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
    register_account_page.continue_btn_click()

    main_page.navigate_to_home_page()
    main_page.my_account_click()
    main_page.my_account_item_click()

    my_account_page = MyAccount(driver)
    my_account_page.edit_account_item_click(3)

    my_account_edit_page = MyAccountEdit(driver)

    new_first_name = user_randomizer.build_random_user_first_name()
    new_last_name = user_randomizer.build_random_user_last_name()
    new_email = user_randomizer.build_random_email_name()

    assert new_first_name != first_name
    assert new_last_name != last_name
    assert new_email != email

    my_account_edit_page.first_name_field_input(new_first_name)
    my_account_edit_page.last_name_field_input(new_last_name)
    my_account_edit_page.email_field_input(new_email)

    actual_result_first_name = my_account_edit_page.first_name_field_read()
    assert actual_result_first_name == new_first_name
    actual_result_last_name = my_account_edit_page.last_name_field_read()
    assert actual_result_last_name == new_last_name
    actual_result_email = my_account_edit_page.email_field_read()
    assert actual_result_email == new_email