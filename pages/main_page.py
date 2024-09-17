from pages.base_page import BasePage
from conftest import driver


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
