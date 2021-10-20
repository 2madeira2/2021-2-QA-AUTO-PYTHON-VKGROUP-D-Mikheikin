import data
import pytest
from base import BaseCase
from locators import locators


class TestOne(BaseCase):
    @pytest.mark.UI
    def test_login(self, login):
        assert self.driver.current_url.startswith("https://target.my.com/dashboard")

    @pytest.mark.UI
    def test_logout(self, login):
        self.wait_element_be_invisible(locators.SPINNER_LOCATOR, 100)
        self.find_n_click(locators.CLICK_LIST_LOGOUT_LOCATOR)
        self.find_n_click(locators.CLICK_BUTTON_LOGOUT_LOCATOR)
        assert self.find(locators.BUTTON_LOG_LOCATOR)

    @pytest.mark.UI
    def test_edit_profile(self, login):
        self.find_n_click(locators.PROFILE_LOCATOR)
        self.send_data_keys(locators.NAME_LOCATOR, data.NAME)
        self.send_data_keys(locators.PHONE_LOCATOR, data.PHONE)
        self.find_n_click(locators.SAVE_PROFILE_LOCATOR)
        self.driver.refresh()
        assert self.find(locators.NAME_LOCATOR).get_attribute('value') == data.NAME
        assert self.find(locators.PHONE_LOCATOR).get_attribute('value') == data.PHONE

    @pytest.mark.UI
    @pytest.mark.parametrize(('tab', 'tab_elem'), [(locators.BALANCE_TAB_LOCATOR, locators.PAYER_INSCRIPTION_LOCATOR),
                                                   (locators.TOOLS_TAB_LOCATOR, locators.TOOLS_ADD_FEED_BUTTON_LOCATOR)])
    def test_tabs(self, login, tab, tab_elem):
        self.find_n_click(tab)
        assert self.find(tab_elem)
