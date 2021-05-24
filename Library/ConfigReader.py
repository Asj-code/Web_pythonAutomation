import configparser


def read_config_data(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigFiles/Config.cfg")
    return config.get(section, key)


def fetch_elements_locators(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigFiles/elements.cfg")
    return config.get(section, key)