import allure
import pytest
from resources import data
from resources import log_messages
from tests.base import BaseCase


@pytest.mark.UI
class TestNegativeLogin(BaseCase):
    authorize = False


    @allure.feature('UI test')
    @allure.description("""We just go on target.com, then we try to login with incorrect login, then we check for 
    the negative result
        """)
    def test_negative_incorrect_login(self):
        with pytest.raises(TimeoutError):
            self.main_page.login('abvgdeyka', 'aboba')
        self.logger.info(log_messages.check("incorrect login"))
        assert self.main_page.page_is_load()
        self.logger.info(log_messages.check_success)

    @allure.feature('UI test')
    @allure.description("""We just go on target.com, then we try to login with incorrect password, then we check for 
    the negative result
        """)
    def test_negative_incorrect_password(self):
        with pytest.raises(TimeoutError):
            self.main_page.login(data.login, 'privetchtotyzdesdelaesh')
        self.logger.info(log_messages.check("incorrect_password"))
        assert 'login/?error_code' in self.driver.current_url
        self.logger.info(log_messages.check_success)


@pytest.mark.UI
class TestCreateSegment(BaseCase):

    @allure.feature('UI test')
    @allure.description("""We just go to target.com, then we go to the segments section, then we create a new segment,
    then we refresh page, check the result and delete added segment
        """)
    def test_create_segment(self, create_segment):
        locator = (create_segment.locators.SEGMENT_TITLE_LOCATOR[0],
                   create_segment.locators.SEGMENT_TITLE_LOCATOR[1].format(create_segment.segment))
        self.driver.refresh()
        self.logger.info(log_messages.check("add segment"))
        assert create_segment.has_element(locator)
        self.logger.info(log_messages.check_success)
        create_segment.delete_segment()


@pytest.mark.UI
class TestDeleteSegment(BaseCase):

    @allure.feature('UI test')
    @allure.description("""We just go to target.com, then we go to the segments section, then we create a new segment,
    then we remove added segment, then refresh page and check the result 
        """)
    def test_delete_segment(self, create_segment):
        locator = (create_segment.locators.SEGMENT_TITLE_LOCATOR[0],
                   create_segment.locators.SEGMENT_TITLE_LOCATOR[1].format(create_segment.segment))
        create_segment.delete_segment()
        self.driver.refresh()
        self.logger.info(log_messages.check("deleted segment"))
        assert not create_segment.has_element(locator)
        self.logger.info(log_messages.check_success)


@pytest.mark.UI
class TestCreateCampaign(BaseCase):

    @allure.feature('UI test')
    @allure.description("""We just go to target.com, then we create new campaign, edit all necessary fields,
    create campaign and check result
        """)
    def test_create_campaign(self, dashboard_page, campaign_page):
        locator = (dashboard_page.locators.CAMPAIGN_TITLE_LOCATOR[0],
                   dashboard_page.locators.CAMPAIGN_TITLE_LOCATOR[1].format(campaign_page.campaign))
        campaign_page.create_new_campaign()
        self.logger.info(log_messages.check("created company"))
        assert dashboard_page.has_element(locator)
        self.logger.info(log_messages.check_success)
