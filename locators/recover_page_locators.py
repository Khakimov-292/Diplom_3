from selenium.webdriver.common.by import By


class RecoverPageLocators:
    RECOVER_BTN = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
