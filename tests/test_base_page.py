from conftest import driver
from data.auth_data import TestAuthData

from pages.base_page import BasePage

from data.url_data import TestUrlData


class TestBasePage:

    def test_mp_form(self, driver):
        auth_page = BasePage(driver)
        auth_page.set_name()
        auth_page.set_pass()
        auth_page.enter_button_click()
        r_url = auth_page.count_url(driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_INVENTORY}'
        auth_page.button_slb_click()
        auth_page.button_basket_click()
        mf_page_p_text = auth_page.set_slb_in_basket()
        assert "Sauce Labs Backpack" in mf_page_p_text.text
        auth_page.button_make_purchase_click()
        auth_page.set_name_op()
        auth_page.set_surname_op()
        auth_page.set_index_op()
        auth_page.button_cont_click()
        auth_page.button_finish_click()
        elem = auth_page.find_elem_cmplt()
        mf_page_div_class = elem.get_attribute("class")
        assert mf_page_div_class == TestAuthData.ACT_CMPLT
