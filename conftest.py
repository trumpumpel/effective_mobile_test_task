import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.chrome.service import Service as ChromeService

from data.url_data import TestUrlData


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920, 990')
    return chrome_options


def _get_driver(name):
    if name == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif name == "firefox":
        service = FireFoxService(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service)


@pytest.fixture(params=["chrome", "firefox"])
def web_driver(request):
    driver = _get_driver(request.param)
    driver.get(f'{TestUrlData.URL}')
    yield driver
    driver.quit()
