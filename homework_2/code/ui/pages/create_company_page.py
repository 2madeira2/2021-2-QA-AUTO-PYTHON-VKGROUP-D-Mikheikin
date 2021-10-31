import os
from ui.pages.base_page import BasePage
from ui.locators.locators import CompanyPageLocators


class CompanyPage(BasePage):

    url = 'https://target.my.com/campaign/new'
    locators = CompanyPageLocators

    def create_new_company(self):
        self.find_n_click(self.locators.TRAFFIC_LOCATOR, 30)
        self.find(self.locators.ADD_URL_LOCATOR).send_keys('https://browser.yandex.ru/')
        self.find_n_click(self.locators.COMPANY_NAME_LOCATOR, 30)
        self.find_n_send_keys(self.locators.COMPANY_NAME_LOCATOR, self.company)
        self.find_n_click(self.locators.BANNER_LOCATOR, 30)
        self.find(self.locators.IMAGE_LOCATOR).send_keys(os.path.abspath(os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'resources/images/yandex_browser.png')))
        self.find_n_click(self.locators.IMAGE_SAVE_BUTTON_LOCATOR)
        self.find_n_click(self.locators.CREATE_BUTTON_LOCATOR)
