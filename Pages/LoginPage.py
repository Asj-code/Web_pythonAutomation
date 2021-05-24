from Library import ConfigReader
from selenium.webdriver.common.by import By


class Login(object):

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_user_name(self, username):
        driver.find_element(By.ID, ConfigReader.fetch_elements_locators("Login", "user_name")).send_keys(username)


    def enter_password(self, password):
        driver.find_element(By.ID, ConfigReader.fetch_elements_locators("Login", "password")).send_keys(password)


    def click_login_btn(self):
        driver.find_element(By.XPATH, "//input[@type='submit']").click()


    def close_browser(self):
        driver.close()


