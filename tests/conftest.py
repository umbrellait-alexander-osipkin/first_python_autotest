import pytest

from selene import browser
from selenium import webdriver
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_cfg():
    browser.config.base_url = 'https://www.google.com'
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.timeout = 15

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()