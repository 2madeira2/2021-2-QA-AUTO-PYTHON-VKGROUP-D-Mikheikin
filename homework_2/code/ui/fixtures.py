import os
import allure
import pytest
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.audience_page import AudiencePage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture
def base_page(driver):
    return BasePage(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def dashboard_page(main_page, config):
    return main_page.login(config['login'], config['password'])


@pytest.fixture
def audience_page(dashboard_page):
    return dashboard_page.go_to_audience()


@pytest.fixture
def company_page(dashboard_page):
    return dashboard_page.go_to_create_company()


@pytest.fixture
def new_segment_page(audience_page):
    return audience_page.create_new_segment()


@pytest.fixture
def create_segment(driver, new_segment_page):
    new_segment_page.create_segment()
    return AudiencePage(driver)


def get_driver(browser_name, download_dir):
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"download.default_directory": download_dir})
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        manager = ChromeDriverManager(version='latest', log_level=0)
        browser = webdriver.Chrome(executable_path=manager.install(), options=options)
    elif browser_name == 'firefox':
        manager = GeckoDriverManager(version='latest', log_level=0)
        browser = webdriver.Firefox(executable_path=manager.install())
    else:
        raise UnsupportedBrowserType(f' Unsupported browser {browser_name}')

    return browser


@pytest.fixture
def driver(config, test_dir):
    browser = get_driver(config['browser'], download_dir=test_dir)
    browser.maximize_window()
    browser.get(config['url'])
    yield browser
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'fail.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'fail.png', allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)


class UnsupportedBrowserType(Exception):
    pass
