import pytest
from selenium import webdriver

from data.url_data import TestUrlData


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920, 990')
    return chrome_options


@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(f'{TestUrlData.URL}')

    yield chrome

    chrome.quit()
