import logging
import allure
from contextlib import contextmanager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from utils.decorators import wait
import utils.static_params as StaticParam

logger = logging.getLogger('test')


class BasePage(object):
    url = 'https://target.my.com/'
    locators = None

    def __init__(self, driver):
        self.driver = driver
        logger.info(f'{self.__class__.__name__} is opening...')
        assert self.page_is_load()

    def page_is_load(self):
        def _check_url():
            if self.driver.current_url != self.url and self.driver.current_url != self.url + '/':
                raise PageNotLoadedException(
                    f'{self.url} did not opened in {StaticParam.BASE_TIMEOUT} for {self.__class__.__name__}.\n'
                    f'Current url: {self.driver.current_url}.')
            return True

        return wait(_check_url, error=PageNotLoadedException, check=True, timeout=StaticParam.BASE_TIMEOUT, interval=0.1)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def find_n_send_keys(self, locator, value):
        inp = self.find(locator)
        inp.clear()
        inp.send_keys(value)

    def has_element(self, locator, timeout=8):
        try:
            self.find(locator, timeout)
        except TimeoutException:
            return False
        return True

    @allure.step('Clicking {locator}')
    def find_n_click(self, locator, timeout=None):
        for i in range(StaticParam.CLICK_RETRY):
            logger.info(f'Clicking on: {locator}. Try: {i + 1} of {StaticParam.CLICK_RETRY}...')
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == StaticParam.CLICK_RETRY - 1:
                    raise

    @property
    def action_chains(self):
        return ActionChains(self.driver)


class PageNotLoadedException(Exception):
    pass
