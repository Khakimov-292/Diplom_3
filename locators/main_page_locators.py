from selenium.webdriver.common.by import By


class MainPageLocators:
    ROOT_FIELD = (By.ID, "root")
    FIRST_BUN_LINK = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[1]/a[1]")
    ACCOUNT_LINK = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    ORDERS_FEED_LINK = (By.XPATH, "//a[@href='/feed']")
    ORDERS_FEED_HEADER = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    INGREDIENT_DETAIL_HEADER = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    CLOSE_MODAL_BTN = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    MODAL_SECTION = (By.XPATH, "//section[contains(@class, 'Modal_modal__P3_V5')]")
    RESULT_ORDER = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]")
    INGREDIENT_COUNTERS = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    BUN_IN_ORDER = (By.XPATH, "//span[contains(text(), 'Флюоресцентная булка R2-D3 (верх)')]")
    ORDER_BTN = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_READY_DIV = (By.XPATH, "//div[@class='Modal_modal__P3_V5']")
