from selenium.webdriver.common.by import By


class BasePageLocators:
    SET_NAME_LOG = (By.CSS_SELECTOR, "input[name='user-name']")
    SET_PAS_LOG = (By.CSS_SELECTOR, "input[name='password']")
    SUB_BTN_CLICK_LOG = (By.CSS_SELECTOR, "input[name='login-button']")
    BASKET_LOC = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
