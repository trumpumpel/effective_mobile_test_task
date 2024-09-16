from data.auth_data import TestAuthData
from pages.base_page import BasePage
from conftest import web_driver
from locators.basket_page_locators import BasketPageLocators


class BasketPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def set_slb_in_basket(self):
        return self.find_element(BasketPageLocators.SLB_LOC_BSKT, 100)

    def button_slb_click(self):
        return self.click_element(BasketPageLocators.BTN_SLB_CL, 100)

    def button_del_bsk_click(self):
        return self.click_element(BasketPageLocators.DEL_LOC_BSKT, 100)

    def find_elem_bskt(self):
        return self.find_element(BasketPageLocators.NO_LOC_BSKT, 100)

    def button_make_purchase_click(self):
        return self.click_element(BasketPageLocators.BTN_MP_LOC, 100)

    def set_name_op(self):
        return self.enter_text(BasketPageLocators.SET_NAME_OP, TestAuthData.COR_NAME_OP, 100)

    def set_surname_op(self):
        return self.enter_text(BasketPageLocators.SET_SURNAME_OP, TestAuthData.COR_SURNAME_OP, 100)

    def set_index_op(self):
        return self.enter_text(BasketPageLocators.SET_INDEX_OP, TestAuthData.COR_INDEX_OP, 100)

    def button_cont_click(self):
        return self.click_element(BasketPageLocators.BTN_CONT_OP, 100)

    def button_finish_click(self):
        return self.click_element(BasketPageLocators.BTN_FIN_OP, 100)

    def find_elem_cmplt(self):
        return self.find_element(BasketPageLocators.EL_CMPT, 100)
