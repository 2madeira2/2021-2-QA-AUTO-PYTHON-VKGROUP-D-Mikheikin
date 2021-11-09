import os
from ui.pages.base_page import BasePage
from ui.locators.locators import CampaignPageLocators
from utils.generate_data import generate_name


class CampaignPage(BasePage):

    url = 'https://target.my.com/campaign/new'
    locators = CampaignPageLocators
    campaign = generate_name()

    def create_new_campaign(self):
        self.find_n_click(self.locators.TRAFFIC_LOCATOR, 10)
        self.find(self.locators.ADD_URL_LOCATOR).send_keys('https://browser.yandex.ru/')
        self.find_n_click(self.locators.CAMPAIGN_NAME_LOCATOR, 30)
        self.find_n_send_keys(self.locators.CAMPAIGN_NAME_LOCATOR, self.campaign)
        self.find_n_click(self.locators.BANNER_LOCATOR, 10)
        self.find(self.locators.IMAGE_LOCATOR).send_keys(os.path.abspath(os.path.join(
            os.path.dirname(os.path.dirname(__file__)), os.pardir, 'resources', 'images', 'yandex_browser.png')))

        self.find_n_click(self.locators.IMAGE_SAVE_BUTTON_LOCATOR)
        self.find_n_click(self.locators.CREATE_BUTTON_LOCATOR)


