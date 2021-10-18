import time
import data
import pytest
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators


CLICK_RETRY = 10


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    @pytest.fixture(scope='function')
    def login(self):
        self.find_n_click(locators.BUTTON_LOG)

        self.send_data_keys(locators.EMAIL_LOC, data.EMAIL)
        self.send_data_keys(locators.PASSWORD_LOC, data.PASSWORD)

        self.find_n_click(locators.BUTTON_AUTH_LOC)

    # поиск элемента по локатору
    def find(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element

    def send_data_keys(self, locator, value):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(value)

    def find_n_click(self, locator):

        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator)
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
            except ElementNotInteractableException:
                if i == CLICK_RETRY - 1:
                    raise
            except ElementClickInterceptedException:
                if i == CLICK_RETRY - 1:
                    raise
