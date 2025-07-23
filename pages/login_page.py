from allure import step

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import urls


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.LOGIN_URL)
        self.wait_for_clickable_element(LoginPageLocators.RECOVER_LINK)

    @step("Открыть восстановление пароля")
    def open_password_recovery(self):
        self.click_element(LoginPageLocators.RECOVER_LINK)
        self.wait_for_load_element(LoginPageLocators.RECOVER_BUTTON)

    @step("Проверка адресов ссылок")
    def is_current_url(self, expected_url):
        self.check_current_url(expected_url)

    @step("Логин пользователя")
    def login(self, email, password):
        self.input_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.input_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.ENTER_BTN)
        self.wait_for_clickable_element(LoginPageLocators.BUN_LINK)
