from ui.pages.base_page import BasePage
from ui.locators.locators import DashboardPageLocators
from ui.pages.audience_page import AudiencePage
from ui.pages.create_company_page import CompanyPage
from selenium.common.exceptions import TimeoutException


class DashboardPage(BasePage):

    url = 'https://target.my.com/dashboard'
    locators = DashboardPageLocators

    def go_to_audience(self):
        self.find_n_click(self.locators.SEGMENTS_LOCATOR)
        return AudiencePage(self.driver)

    def go_to_create_company(self):
        try:
            self.find_n_click(self.locators.CREATE_COMPANY_BUTTON_LOCATOR)
        except TimeoutException:
            self.find_n_click(self.locators.CREATE_COMPANY_BUTTON_LOCATOR)
        return CompanyPage(self.driver)
