from allure import step

from helpers import generate_email
from pages.base_page import BasePage
from locators.recover_page_locators import RecoverPageLocators
from data import urls


class RecoverPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.RECOVER_URL)
        self.wait_for_load_element(RecoverPageLocators.RECOVER_BTN)

        email = generate_email()
        self.input_to_element(RecoverPageLocators.EMAIL_INPUT, email)
        self.click_element(RecoverPageLocators.RECOVER_BTN)
        self.wait_for_load_element(RecoverPageLocators.SAVE_BTN)

    @step("Ввод почты")
    def enter_email(self, email):
        self.input_to_element(RecoverPageLocators.EMAIL_INPUT, email)

    @step("Клик на кнопку 'восстановить'")
    def click_to_recover(self):
        self.click_element(RecoverPageLocators.RECOVER_BTN)
        self.wait_for_load_element(RecoverPageLocators.SAVE_BTN)

    @step("Ввод пароля")
    def enter_password(self, pwd):
        self.input_to_element(RecoverPageLocators.PASSWORD_INPUT, pwd)

    @step("Клик по кнопке показать/скрыть пароль делает поле активным")
    def click_show_password(self):
        self.click_element(RecoverPageLocators.SHOW_PASSWORD_BTN)
        element_class = self.get_attribute_class(RecoverPageLocators.RECOVER_BTN)
        return element_class

    @step("Проверка адресов ссылок")
    def is_current_url(self, expected_url):
        self.check_current_url(expected_url)
