from allure import step

from pages.base_page import BasePage
from locators.recover_page_locators import RecoverPageLocators
from locators.reset_page_locators import ResetPageLocators
from data import urls


class RecoverPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.RECOVER_URL)
        self.wait_for_load_element(RecoverPageLocators.RECOVER_BTN)

    @step("Ввод почты")
    def enter_email(self, email):
        self.input_to_element(RecoverPageLocators.EMAIL_INPUT, email)

    @step("Клик на кнопку 'восстановить'")
    def click_to_recover(self):
        self.click_element(RecoverPageLocators.RECOVER_BTN)
        self.wait_for_load_element(ResetPageLocators.SAVE_BTN)
