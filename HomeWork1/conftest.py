from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(executable_path=r'C:\ChromeDriver\chromedriver.exe')
    driver.get("https://target.my.com/")
    driver.maximize_window()
    yield driver
    driver.close()
