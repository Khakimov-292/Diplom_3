from allure import title
from data import urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainFunctionality:
    @title("Переход по клику на 'Конструктор'")
    def test_constructor_link(self, driver):
        page = MainPage(driver)
        page.click_to_constructor()
        assert driver.current_url == urls.MAIN_URL

    @title("Переход в ленту заказов")
    def test_orders_feed(self, driver):
        page = MainPage(driver)
        page.click_to_orders_feed()
        assert driver.current_url == urls.FEED_URL

    @title("Открыть всплывающее окно ингредиентов")
    def test_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.click_to_first_ingredient()
        assert "ingredient" in driver.current_url

    @title("Закрыть всплывающее окно")
    def test_close_modal(self, driver):
        page = MainPage(driver)
        page.click_to_first_ingredient()
        page.close_ingredient_modal()
        assert page.is_modal_closed()

    @title("Проверка сетчика ингредиентов")
    def test_ingredients_counter(self, driver):
        page = MainPage(driver)
        page.add_buns_to_order()
        assert page.get_first_bun_counter() == 2

    @title("Проверка создания заказа")
    def test_create_order(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        page = MainPage(driver)
        page.add_buns_to_order()
        page.make_order()
        assert page.is_order_accepted()
