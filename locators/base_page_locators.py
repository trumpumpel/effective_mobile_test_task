from selenium.webdriver.common.by import By


class BasePageLocators:
    SET_NAME_LOG = (By.CSS_SELECTOR, "input[name='user-name']")
    SET_PAS_LOG = (By.CSS_SELECTOR, "input[name='password']")
    SUB_BTN_CLICK_LOG = (By.CSS_SELECTOR, "input[name='login-button']")
    # BTN_SLB_CL = (By.XPATH, "//button[text()='Add to cart']")
    BASKET_LOC = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    # SLB_LOC_BSKT = (By.XPATH, "//div[@class='inventory_item_name']")
    # DEL_LOC_BSKT = (By.XPATH, "//button[@class='btn btn_secondary btn_small cart_button']")
    # NO_LOC_BSKT = (By.XPATH, "//div[@class='removed_cart_item']")
    # BTN_MP_LOC = (By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button ']")
    # SET_NAME_OP = (By.CSS_SELECTOR, "input[name='firstName']")
    # SET_SURNAME_OP = (By.CSS_SELECTOR, "input[name='lastName']")
    # SET_INDEX_OP = (By.CSS_SELECTOR, "input[name='postalCode']")
    # BTN_CONT_OP = (By.CSS_SELECTOR, "input[name='continue']")
    # BTN_FIN_OP = (By.CSS_SELECTOR, "button[name='finish']")
    # EL_CMPT = (By.XPATH, "//h2[@class='complete-header']")
