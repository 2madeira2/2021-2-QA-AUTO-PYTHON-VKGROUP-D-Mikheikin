import data
import pytest
from base import BaseCase
from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOne(BaseCase):
    @pytest.mark.UI
    def test_log(self, login):
        assert self.driver.current_url == "https://target.my.com/dashboard"

    @pytest.mark.UI
    def test_logout(self, login):
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.invisibility_of_element_located(locators.SPINNER_LOC))
        self.find_n_click(locators.CLICK_LIST_LOGOUT)
        self.find_n_click(locators.CLICK_BUTTON_LOGOUT)
        assert self.find(locators.BUTTON_LOG)

    @pytest.mark.UI
    def test_edit_profile(self, login):
        self.find_n_click(locators.PROFILE_LOC)
        self.send_data_keys(locators.NAME_LOC, data.NAME)
        self.send_data_keys(locators.PHONE_LOC, data.PHONE)
        self.find_n_click(locators.SAVE_LOC)
        self.driver.refresh()
        assert self.find(locators.NAME_LOC).get_attribute('value') == data.NAME \
               and self.find(locators.PHONE_LOC).get_attribute('value') == data.PHONE

    @pytest.mark.UI
    @pytest.mark.parametrize(('tab', 'tab_elem'), [(locators.BALANCE_TAB_LOC, locators.PAYER_INSCRIPTION),
                                                   (locators.TOOLS_TAB_LOC, locators.TOOLS_ADD_FEED_BUTTON)])
    def test_tabs(self, login, tab, tab_elem):
        self.find_n_click(tab)
        assert self.find(tab_elem)
