from allure import title
from data import urls
from data.constants import Constant
from pages.login_page import LoginPage
from pages.recover_page import RecoverPage
from helpers import generate_email


class TestRecoverPage:

    @title("Переход на страницу восстановления пароля")
    def test_recover_link(self, driver):
        page = LoginPage(driver)
        page.open_password_recovery()
        assert driver.current_url == urls.RECOVER_URL

    @title("Ввод почты и клик по кнопке «Восстановить»")
    def test_request_password_recover(self, driver):
        page = RecoverPage(driver)
        email = generate_email()
        page.enter_email(email)
        page.click_to_recover()
        assert driver.current_url == urls.RESET_URL

    @title("Показать/скрыть пароль")
    def test_click_the_show_hidden_button_field_active(self, driver):
        page = RecoverPage(driver)
        page.enter_password("test")
        element_class = page.click_show_password()
        assert element_class == Constant.field_password_active
