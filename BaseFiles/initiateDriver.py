from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader


def start_browser():
    global driver
    if ConfigReader.read_config_data("Details", "Browser") == "Chrome":
        path = "Drivers/chromedriver"
        driver = Chrome(executable_path=path)
    elif ConfigReader.read_config_data("Details", "Browser") == "Firefox":
        path = "Drivers/geckodriver"
        driver = Firefox(executable_path=path)
    else:
        path = "Drivers/chromedriver"
        driver = Chrome(executable_path=path)

    driver.get(ConfigReader.read_config_data("Details", "Application_URL"))
    driver.maximize_window()
    return driver
