import pytest
from selenium import webdriver
from api import API
from helpers import generate_random_string


def get_driver(browser):
    if browser == "firefox":
        return webdriver.Firefox()
    elif browser == "chrome":
        return webdriver.Chrome()
    raise ValueError("this browser is not supported")


@pytest.fixture(params=("chrome", "firefox"))
def driver(request):
    driver = get_driver(request.param)
    yield driver
    driver.quit()


@pytest.fixture
def user():
    email = f"{generate_random_string(5)}@ya.ru"
    password = f"{generate_random_string(8)}"
    name = f"{generate_random_string(10)}"

    api = API()
    api.register_user(email, password, name)
    yield {
        "email": email,
        "password": password,
        "name": name,
    }

    api.login_user(email, password)
    api.delete_user()
