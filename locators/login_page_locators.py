from selenium.webdriver.common.by import By


class LoginPageLocators:
    RECOVER_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BTN = (By.XPATH, "//button[contains(text(), 'Войти')]")
