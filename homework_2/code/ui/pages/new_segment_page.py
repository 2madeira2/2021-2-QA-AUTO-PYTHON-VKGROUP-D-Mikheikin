from ui.pages.base_page import BasePage
from ui.locators.locators import NewSegmentPageLocators


class NewSegmentPage(BasePage):
    url = 'https://target.my.com/segments/segments_list/new'
    locators = NewSegmentPageLocators

    def __init__(self, driver, segment):
        self.segment = segment
        super().__init__(driver)

    def create_segment(self):
        self.find_n_click(self.locators.SEGMENT_CHECKBOX_LOCATOR)
        self.find_n_click(self.locators.SEGMENT_SUBMIT_2_LOCATOR)
        self.find_n_send_keys(self.locators.SEGMENT_INPUT_LOCATOR, self.segment)
        self.find_n_click(self.locators.SEGMENT_SUBMIT_1_LOCATOR)
