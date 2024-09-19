from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import driver
from data.auth_data import TestAuthData
from locators.locators import Locators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url: str):
        self.driver.get(url)

    def find_element(self, locator: tuple, timeout: 15) -> object:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple, timeout: 15):
        element = self.find_element(locator, timeout)
        element.click()

    def enter_text(self, locator: tuple, text: str, timeout: 15):
        element = self.find_element(locator, timeout)
        element.click()
        element.send_keys(text)

    def count_url(self, web_driver):
        return web_driver.current_url

    def button_basket_click(self):
        return self.click_element(Locators.BASKET_LOC, 100)

    def set_name(self):
        return self.enter_text(Locators.SET_NAME_LOGIN, TestAuthData.NAME, 100)

    def set_pass(self):
        return self.enter_text(Locators.SET_PAS_LOGIN, TestAuthData.PASSWORD, 100)

    def enter_button_click(self):
        return self.click_element(Locators.SUB_BTN_CLICK_LOG, 100)

    def set_slb_in_basket(self):
        return self.find_element(Locators.SLB_LOC_BSKT, 100)

    def button_slb_click(self):
        return self.click_element(Locators.BTN_SLB_CL, 100)

    def button_del_bsk_click(self):
        return self.click_element(Locators.DEL_LOC_BSKT, 100)

    def find_elem_bskt(self):
        return self.find_element(Locators.NO_LOC_BSKT, 100)

    def button_make_purchase_click(self):
        return self.click_element(Locators.BTN_MP_LOC, 100)

    def set_name_op(self):
        return self.enter_text(Locators.SET_NAME_OP, TestAuthData.NAME_OP, 100)

    def set_surname_op(self):
        return self.enter_text(Locators.SET_SURNAME_OP, TestAuthData.SURNAME_OP, 100)

    def set_index_op(self):
        return self.enter_text(Locators.SET_INDEX_OP, TestAuthData.INDEX_OP, 100)

    def button_cont_click(self):
        return self.click_element(Locators.BTN_CONT_OP, 100)

    def button_finish_click(self):
        return self.click_element(Locators.BTN_FIN_OP, 100)

    def find_elem_cmplt(self):
        return self.find_element(Locators.EL_CMPT, 100)
