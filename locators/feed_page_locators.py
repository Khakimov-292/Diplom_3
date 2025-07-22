from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDERS_FEED_HEADER = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    ORDERS_COUNTER = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ALL_ORDERS = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")
    ORDER_MODAL_OPENED = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li["
                                   "@class='text text_type_digits-default mb-2']")
    ORDER_BY_NUMBER = (By.XPATH, "//p[contains(text(), '{}')]")
