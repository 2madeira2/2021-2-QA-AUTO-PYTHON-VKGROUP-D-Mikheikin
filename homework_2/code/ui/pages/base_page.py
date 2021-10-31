import logging
import allure
from contextlib import contextmanager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from ui.locators.locators import BasePageLocators
from utils.decorators import wait

import random
import string

CLICK_RETRY = 3
BASE_TIMEOUT = 5

logger = logging.getLogger('test')


class BasePage(object):
    url = 'https://target.my.com/'
    locators = BasePageLocators()
    segment = ''.join(random.sample(string.ascii_letters + string.digits, 15))
    company = ''.join(random.sample(string.ascii_letters + string.digits, 15))

    def __init__(self, driver):
        self.driver = driver
        with allure.step(f'Going to {self.__class__.__name__} page'):
            logger.info(f'{self.__class__.__name__} is opening...')
        assert self.page_is_load()

    def page_is_load(self):
        def _check_url():
            if self.driver.current_url != self.url and self.driver.current_url != self.url + '/':
                raise PageNotLoadedException(
                    f'{self.url} did not opened in {BASE_TIMEOUT} for {self.__class__.__name__}.\n'
                    f'Current url: {self.driver.current_url}.')
            return True

        return wait(_check_url, error=PageNotLoadedException, check=True, timeout=BASE_TIMEOUT, interval=0.1)

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
        for i in range(CLICK_RETRY):
            logger.info(f'Clicking on: {locator}. Try: {i + 1} of {CLICK_RETRY}...')
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    @contextmanager
    def switch_to_next(self, current, closed=True):
        for x in self.driver.window_handles:
            if x != current:
                self.driver.switch_to.window(x)
                break
        yield
        if closed:
            self.driver.close()
        self.driver.switch_to.window(current)


class PageNotLoadedException(Exception):
    pass
