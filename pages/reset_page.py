from allure import step

from pages.base_page import BasePage
from locators.reset_page_locators import ResetPageLocators
from locators.recover_page_locators import RecoverPageLocators
from data import urls
from helpers import generate_email


class ResetPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.RECOVER_URL)
        self.wait_for_load_element(RecoverPageLocators.RECOVER_BTN)

        email = generate_email()
        self.input_to_element(RecoverPageLocators.EMAIL_INPUT, email)
        self.click_element(RecoverPageLocators.RECOVER_BTN)
        self.wait_for_load_element(ResetPageLocators.SAVE_BTN)

    @step("Ввод пароля")
    def enter_password(self, pwd):
        self.input_to_element(ResetPageLocators.PASSWORD_INPUT, pwd)

    @step("Клик на иконку показать пароль")
    def click_show_password(self):
        self.click_element(ResetPageLocators.SHOW_PASSWORD_BTN)
