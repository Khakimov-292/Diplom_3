from allure import title
from data import urls
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage


class TestAccountPage:
    @title("Переход в личный кабинет")
    def test_account_link(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        main_page = MainPage(driver)
        main_page.click_to_account()
        assert main_page.is_current_url(urls.ACCOUNT_URL)

    @title("Переход в историю заказов")
    def test_order_history(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        main_page = MainPage(driver)
        main_page.click_to_account()
        account_page = AccountPage(driver)
        account_page.click_to_orders()
        assert account_page.current_url(urls.ORDER_HISTORY_URL)

    @title("Выход из системы")
    def test_logout(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        account_page = AccountPage(driver)
        account_page.logout()
        assert account_page.current_url(urls.LOGIN_URL)
