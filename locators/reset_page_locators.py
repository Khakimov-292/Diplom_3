from selenium.webdriver.common.by import By


class ResetPageLocators:
    SAVE_BTN = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    PASSWORD_INPUT_PARENT = (By.XPATH, "//input[@name='Введите новый пароль']/..")
    SHOW_PASSWORD_BTN = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    