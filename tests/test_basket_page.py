import time

from conftest import web_driver

from data.url_data import TestUrlData
from pages.basket_page import BasketPage

from data.auth_data import TestAuthData
from data.url_data import TestUrlData


class TestMainPage:
    def test_fnd_add_slb(self, web_driver):
        mf_page = BasketPage(web_driver)
        mf_page.set_name()
        mf_page.set_pas()
        mf_page.enter_button_click()
        mf_page.button_slb_click()
        mf_page.button_basket_click()
        mf_page_p_text = mf_page.set_slb_in_basket()
        assert "Sauce Labs Backpack" in mf_page_p_text.text

    def test_del_slb_bsk(self, web_driver):
        mf_page = BasketPage(web_driver)
        mf_page.set_name()
        mf_page.set_pas()
        mf_page.enter_button_click()
        mf_page.button_slb_click()
        mf_page.button_basket_click()
        mf_page.button_del_bsk_click()
        elem = mf_page.find_elem_bskt()
        mf_page_div_class = elem.get_attribute("class")
        assert mf_page_div_class == TestAuthData.ACT_WIN

    def test_mp_form(self, web_driver):
        mf_page = BasketPage(web_driver)
        mf_page.set_name()
        mf_page.set_pas()
        mf_page.enter_button_click()
        mf_page.button_slb_click()
        mf_page.button_basket_click()
        mf_page.button_make_purchase_click()
        mf_page.set_name_op()
        mf_page.set_surname_op()
        mf_page.set_index_op()
        mf_page.button_cont_click()
        mf_page.button_finish_click()
        elem = mf_page.find_elem_cmplt()
        mf_page_div_class = elem.get_attribute("class")
        assert mf_page_div_class == TestAuthData.ACT_CMPLT
