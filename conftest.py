from selenium import webdriver
import pytest

from data.user_data_randomizer import UserDataRandomizer


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def user_randomizer():
    user_randomizer = UserDataRandomizer()
    return user_randomizer


