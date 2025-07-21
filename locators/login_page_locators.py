from selenium.webdriver.common.by import By


class LoginPageLocators:
    RECOVER_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    BUN_LINK = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[1]/a[1]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    RECOVER_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")
    ENTER_BTN = (By.XPATH, "//button[contains(text(), 'Войти')]")
