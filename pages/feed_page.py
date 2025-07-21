from allure import step
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
from data import urls


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.FEED_URL)
        self.wait_for_clickable_element(FeedPageLocators.ORDERS_FEED_HEADER)

    @step("Получить количество заказов")
    def get_orders_count(self):
        self.wait_for_load_element(FeedPageLocators.ORDERS_COUNTER)
        counters = self.find_elements(FeedPageLocators.ORDERS_COUNTER)
        if len(counters) != 2:
            return 0, 0
        return int(counters[0].text), int(counters[1].text)

    @step("Открыть последний заказ")
    def open_last_order(self):
        orders = self.find_elements(FeedPageLocators.ALL_ORDERS)
        orders[0].click()
        self.wait_for_load_element(FeedPageLocators.ORDER_MODAL_OPENED)

    @step("Пробуем найти заказ на странице")
    def is_order_exist(self, number):
        locator = f"//p[contains(text(), '{number}')]"
        try:
            self.find_elements((By.XPATH, locator))
        except NoSuchElementException:
            return False
        return True

    @step("Получить номер заказа в работе")
    def get_order_number_in_progress(self, number):
        self.wait_for_load_element(FeedPageLocators.ORDER_IN_PROGRESS)
        numbers = self.find_elements(FeedPageLocators.ORDER_IN_PROGRESS)
        if len(numbers) == 0:
            return "0"
        return numbers[0].text
