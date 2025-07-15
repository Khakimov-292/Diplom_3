from allure import step

from locators.account_page_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        page = MainPage(driver)
        page.click_to_account()

    @step("Логаут пользователя")
    def logout(self):
        self.click_element(AccountPageLocators.LOGOUT_LINK)
        self.wait_for_clickable_element(LoginPageLocators.ENTER_BTN)

    @step("Перейти в историю заказов")
    def click_to_orders(self):
        self.click_element(AccountPageLocators.ORDERS_LINK)
        self.wait_for_load_element(AccountPageLocators.ORDERS_ACTIVE_LINK)

    @step("Получить номер последнего заказа")
    def get_last_order_number(self):
        self.wait_for_clickable_element(AccountPageLocators.ALL_ORDERS_NUMBER)
        all_orders = self.find_elements(AccountPageLocators.ALL_ORDERS_NUMBER)
        if len(all_orders) == 0:
            return "0"
        return all_orders[0].text
