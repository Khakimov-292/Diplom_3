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
        feed_page = FeedPage(driver)
        feed_page.open_last_order()

    @title("Заказы пользователя отображаются в ленте заказов")
    def test_users_order_in_order_feed(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        main_page = MainPage(driver)
        main_page.add_buns_to_order()
        main_page.make_order()
        account_page = AccountPage(driver)
        account_page.click_to_orders()
        last_order_number = account_page.get_last_order_number()
        feed_page = FeedPage(driver)
        assert feed_page.is_order_exist(last_order_number)

    @title("Проверка увеличения счетчика за всё время")
    def test_total_counter(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        feed_page = FeedPage(driver)
        old_total, _ = feed_page.get_orders_count()
        main_page = MainPage(driver)
        main_page.add_buns_to_order()
        main_page.make_order()
        new_total, _ = feed_page.get_orders_count()
        assert old_total < new_total

    @title("Проверка увеличения счетчика за сегодня")
    def test_daily_counter(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        feed_page = FeedPage(driver)
        _, old_daily = feed_page.get_orders_count()
        main_page = MainPage(driver)
        main_page.add_buns_to_order()
        main_page.make_order()
        _, new_daily = feed_page.get_orders_count()
        assert old_daily < new_daily

    @title("Проверка номера оформленного заказа в разделе В работе")
    def test_order_in_progress(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        main_page = MainPage(driver)
        main_page.add_buns_to_order()
        main_page.make_order()
        account_page = AccountPage(driver)
        account_page.click_to_orders()
        last_order_number = account_page.get_last_order_number()
        feed_page = FeedPage(driver)
        order_in_progress = feed_page.get_order_number_in_progress(last_order_number[1:])
        assert last_order_number[1:] == order_in_progress
