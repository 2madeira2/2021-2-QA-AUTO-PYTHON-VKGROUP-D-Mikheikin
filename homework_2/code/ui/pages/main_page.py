from ui.pages.base_page import BasePage
from ui.locators.locators import MainPageLocators
from ui.pages.dashboard_page import DashboardPage


class MainPage(BasePage):

    locators = MainPageLocators

    def login(self, login, password):
        self.find_n_click(self.locators.LOGIN_ENTRY_BUTTON_LOCATOR)
        self.find(self.locators.LOGIN_LOCATOR).send_keys(login)
        self.find(self.locators.PASSWORD_LOCATOR).send_keys(password)
        self.find_n_click(self.locators.SUBMIT_BUTTON_LOCATOR)
        return DashboardPage(self.driver)
