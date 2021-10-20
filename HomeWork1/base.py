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
        self.find_n_click(locators.BUTTON_LOG_LOCATOR)

        self.send_data_keys(locators.EMAIL_LOCATOR, data.EMAIL)
        self.send_data_keys(locators.PASSWORD_LOCATOR, data.PASSWORD)

        self.find_n_click(locators.BUTTON_AUTH_LOCATOR)

    # поиск элемента по локатору
    def find(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def send_data_keys(self, locator, value, timeout=15):
        elem = self.find(locator, timeout)
        elem.clear()
        elem.send_keys(value)

    def find_n_click(self, locator, timeout=15):

        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator, timeout)
                elem.click()
                return
            except (StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException):
                if i == CLICK_RETRY - 1:
                    raise

    def wait_element_be_invisible(self, locator, timeout):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(locator))
