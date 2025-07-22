from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @step('Переходим в личный кабинет')
    def check_account_page_open(self):
        self.click_element(AccountPageLocators.ACCOUNT_LINK)
        self.wait_for_clickable_element(AccountPageLocators.PROFILE_BUTTON)

    @step("Логаут пользователя")
    def logout(self):
        self.click_element(AccountPageLocators.LOGOUT_LINK)
        self.wait_for_clickable_element(AccountPageLocators.ENTER_FORM)

    @step()

    @step("Перейти в историю заказов")
    def click_to_orders(self):
        self.click_element(AccountPageLocators.ORDERS_LINK)
        self.wait_for_load_element(AccountPageLocators.ORDERS_ACTIVE_LINK)

    @step("Проверка адресов ссылок")
    def current_url(self, expected_url):
        self.check_current_url(expected_url)

    @step("Получить номер последнего заказа")
    def get_last_order_number(self):
        self.wait_for_clickable_element(AccountPageLocators.ALL_ORDERS_NUMBER)
        all_orders = self.find_elements(AccountPageLocators.ALL_ORDERS_NUMBER)
        if len(all_orders) == 0:
            return "0"
        return all_orders[0].text
