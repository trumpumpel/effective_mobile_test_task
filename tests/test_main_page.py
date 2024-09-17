from conftest import driver

from pages.main_page import MainPage

from data.url_data import TestUrlData


class TestMainPage:

    def test_click_aut(self, driver):
        mf_page = MainPage(driver)
        mf_page.set_name()
        mf_page.set_pas()
        mf_page.enter_button_click()
        r_url = mf_page.count_url(driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_IN}'
