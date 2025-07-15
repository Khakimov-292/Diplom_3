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

        page = MainPage(driver)
        page.click_to_account()
        assert driver.current_url == urls.ACCOUNT_URL

    @title("Переход в историю заказов")
    def test_order_history(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        page = MainPage(driver)
        page.click_to_account()

        page = AccountPage(driver)
        page.click_to_orders()
        assert driver.current_url == urls.ORDER_HISTORY_URL

    @title("Выход из системы")
    def test_logout(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        page = AccountPage(driver)
        page.logout()
        assert driver.current_url == urls.LOGIN_URL
