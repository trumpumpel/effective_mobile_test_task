from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import driver
import allure
from data.auth_data import TestAuthData
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открываем страницу")
    def navigate(self, url: str):
        self.driver.get(url)

    @allure.step("Ищем элемент на странице")
    def find_element(self, locator: tuple, timeout: 15) -> object:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ищем и кликаем по найденому элементу")
    def click_element(self, locator: tuple, timeout: 15):
        element = self.find_element(locator, timeout)
        element.click()

    @allure.step("Вводим текст")
    def enter_text(self, locator: tuple, text: str, timeout: 15):
        element = self.find_element(locator, timeout)
        element.click()
        element.send_keys(text)

    @allure.step('Получаю текущий урл')
    def count_url(self, web_driver):
        return web_driver.current_url

    def button_basket_click(self):
        return self.click_element(BasePageLocators.BASKET_LOC, 100)

    @allure.step('Вводим email')
    def set_name(self):
        return self.enter_text(BasePageLocators.SET_NAME_LOG, TestAuthData.COR_NAME, 100)

    @allure.step('Вводим пароль')
    def set_pas(self):
        return self.enter_text(BasePageLocators.SET_PAS_LOG, TestAuthData.COR_PASSWORD, 100)

    @allure.step('Клик по кнопке Ввод')
    def enter_button_click(self):
        return self.click_element(BasePageLocators.SUB_BTN_CLICK_LOG, 100)
