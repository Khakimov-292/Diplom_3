from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_for_load_element(self, locator):
        self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def drag_and_drop(self, drag, drop):
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    def wait_for_clickable_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        return self.driver.find_element(*locator).click()

    def input_to_element(self, locator, data):
        return self.driver.find_element(*locator).send_keys(data)

    def scroll_to_element(self, locator):
        return self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            self.find_elements(locator)
        )

    def get_attribute_class(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(MainPageLocators.OVERLAYING_ELEMENT))
        element_class = self.find_elements(locator).get_attribute('class')
        return element_class

    def check_current_url(self, expected_url):
        return self.driver.current_url == expected_url
