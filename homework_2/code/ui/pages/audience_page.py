from ui.pages.base_page import BasePage
from ui.locators.locators import AudiencePageLocators
from ui.pages.new_segment_page import NewSegmentPage
from selenium.common.exceptions import TimeoutException
from utils.generate_data import generate_name


class AudiencePage(BasePage):

    url = 'https://target.my.com/segments/segments_list'
    locators = AudiencePageLocators
    segment = generate_name()

    def create_new_segment(self):
        try:
            self.find_n_click(self.locators.NEW_SEGMENT_LOCATOR)
        except TimeoutException:
            self.find_n_click(self.locators.NEW_SEGMENT_BUTTON_LOCATOR)
        return NewSegmentPage(self.driver, self.segment)

    def delete_segment(self):
        locator = (self.locators.SEGMENT_CROSS_LOCATOR[0],
                   self.locators.SEGMENT_CROSS_LOCATOR[1].format(self.segment))
        self.find_n_click(locator)
        self.find_n_click(self.locators.SEGMENT_DELETE_LOCATOR)
