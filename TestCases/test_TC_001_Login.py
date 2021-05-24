from BaseFiles import initiateDriver
from Pages import LoginPage
import pytest


def data_generator():
    data_list = [["standard_user", "secret_sauce"], ["", "secret_sauce"], ["standard_user", ""]]
    return data_list


@pytest.mark.parametrize("data", data_generator())
def test_valid_login(data):
    driver = initiateDriver.start_browser()
    login = LoginPage.Login(driver)
    login.enter_user_name(data[0])
    login.enter_password(data[1])
    login.click_login_btn()
    login.close_browser()