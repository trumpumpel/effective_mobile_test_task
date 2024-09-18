from conftest import driver

from pages.base_page import BasePage

from data.url_data import TestUrlData


class TestBasePage:

    def test_click_aut(self, driver):
        mf_page = BasePage(driver)
        mf_page.set_name()
        mf_page.set_pas()
        mf_page.enter_button_click()
        r_url = mf_page.count_url(driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_IN}'
