from conftest import web_driver

from pages.main_page import MainPage

from data.url_data import TestUrlData


class TestMainPage:

    def test_click_aut(self, web_driver):
        mf_page = MainPage(web_driver)
        mf_page.set_name()
        mf_page.set_pas()
        mf_page.enter_button_click()
        r_url = mf_page.count_url(web_driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_IN}'
