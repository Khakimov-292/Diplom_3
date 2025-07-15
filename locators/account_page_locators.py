from selenium.webdriver.common.by import By


class AccountPageLocators:
    ORDERS_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_LINK = (By.XPATH, "//button[contains(text(), 'Выход')]")
    ORDERS_ACTIVE_LINK = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive "
                                    "Account_link_active__2opc9']")
    ALL_ORDERS_NUMBER = (By.XPATH, "//p[@class='text text_type_digits-default']")
