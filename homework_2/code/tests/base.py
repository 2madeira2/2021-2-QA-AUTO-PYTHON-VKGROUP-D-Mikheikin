import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.main_page import MainPage
from ui.pages.dashboard_page import DashboardPage


class BaseCase:
    driver = None
    config = None
    logger = None
    main_page = None
    dashboard_page = None

    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger
        self.main_page: MainPage = request.getfixturevalue('main_page')
        if self.authorize:
            self.dashboard_page: DashboardPage = request.getfixturevalue('dashboard_page')
