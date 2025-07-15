from allure import title
from pages.login_page import LoginPage
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.account_page import AccountPage


class TestFeedPage:
    @title("Проверка открытия заказа")
    def test_open_order(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        page = FeedPage(driver)
        page.open_last_order()

    @title("Заказы пользователя отображаются в ленте заказов")
    def test_users_order_in_order_feed(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        page = MainPage(driver)
        page.add_buns_to_order()
        page.make_order()

        page = AccountPage(driver)
        page.click_to_orders()
        last_order_number = page.get_last_order_number()

        page = FeedPage(driver)
        assert page.is_order_exist(last_order_number)

    @title("Проверка увелечения счетчика за всё время")
    def test_total_counter(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        page = FeedPage(driver)
        old_total, _ = page.get_orders_count()

        page = MainPage(driver)
        page.add_buns_to_order()
        page.make_order()

        page = FeedPage(driver)
        new_total, _ = page.get_orders_count()
        assert old_total < new_total

    @title("Проверка увелечения счетчика за сегодня")
    def test_daily_counter(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        page = FeedPage(driver)
        _, old_daily = page.get_orders_count()

        page = MainPage(driver)
        page.add_buns_to_order()
        page.make_order()

        page = FeedPage(driver)
        _, new_daily = page.get_orders_count()
        assert old_daily < new_daily

    @title("Проверка номера оформленного заказа в разделе В работе")
    def test_order_in_progress(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        page = MainPage(driver)
        page.add_buns_to_order()
        page.make_order()

        page = AccountPage(driver)
        page.click_to_orders()
        last_order_number = page.get_last_order_number()

        page = FeedPage(driver)
        order_in_progress = page.get_order_number_in_progress(last_order_number[1:])
        assert last_order_number[1:] == order_in_progress
