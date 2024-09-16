from pages.base_page import BasePage
from conftest import web_driver


class MainPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)
