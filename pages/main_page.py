from allure import step
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import urls


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.MAIN_URL)
        self.wait_for_clickable_element(MainPageLocators.ROOT_FIELD)

    @step("Перейти в конструктор")
    def click_to_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)
        self.wait_for_clickable_element(MainPageLocators.ROOT_FIELD)

    @step("Перейти в личный кабинет")
    def click_to_account(self):
        self.wait_for_clickable_element(MainPageLocators.ACCOUNT_LINK)
        self.click_element(MainPageLocators.ACCOUNT_LINK)
        self.wait_for_load_element(MainPageLocators.OUT_LINK)

    @step("Получение текущего адреса ссылки")
    def get_current_url(self):
        return self.driver.current_url

    @step("Перейти в ленту заказов")
    def click_to_orders_feed(self):
        self.wait_for_clickable_element(MainPageLocators.ORDERS_FEED_LINK)
        self.click_element(MainPageLocators.ORDERS_FEED_LINK)
        self.wait_for_load_element(MainPageLocators.ORDERS_FEED_HEADER)

    @step("Клик по ингридиенту")
    def click_to_first_ingredient(self):
        self.wait_for_clickable_element(MainPageLocators.FIRST_BUN_LINK)
        self.click_element(MainPageLocators.FIRST_BUN_LINK)
        self.wait_for_load_element(MainPageLocators.INGREDIENT_DETAIL_HEADER)

    @step("Закрыть окно ингредиента")
    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BTN)

    @step("Проверка адресов ссылок")
    def is_current_url(self, expected_url):
        self.check_current_url(expected_url)

    @step("Добавление булочки в заказ")
    def add_buns_to_order(self):
        drag = self.find_elements(MainPageLocators.FIRST_BUN_LINK)
        drop = self.find_elements(MainPageLocators.RESULT_ORDER)
        self.drag_and_drop(drag, drop)
        self.wait_for_load_element(MainPageLocators.BUN_IN_ORDER)

    @step("Оформить заказ")
    def make_order(self):
        self.click_element(MainPageLocators.ORDER_BTN)

    @step("Получить счетчик первой булочки")
    def get_first_bun_counter(self):
        counters = self.find_elements(MainPageLocators.INGREDIENT_COUNTERS)
        if len(counters) == 0:
            return 0
        return int(counters[0].text)

    def is_modal_closed(self):
        el = self.find_elements(MainPageLocators.MODAL_SECTION)
        return "Modal_modal_opened__3ISw4" not in el.get_attribute("class")

    def is_order_accepted(self):
        self.wait_for_load_element(MainPageLocators.ORDER_READY_DIV)
        return True
