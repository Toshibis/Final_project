from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    BASKET_LINK_MP = (By.XPATH, "//a[@class='btn btn-default']")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.XPATH, "//input[@id='id_registration-email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='id_registration-password1']")
    RE_PASSWORD_FIELD = (By.XPATH, "//input[@id='id_registration-password2']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    SIGN_UP_IS_OK = (By.XPATH, "//i[@class='icon-ok-sign']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    TITLE_BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    TITLE_BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    BOOK_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    BASKET_LINK_PP = (By.XPATH, "//a[@class='btn btn-default']")


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p/text()')
    BASKET_WITH_PRODUCT = (By.XPATH, "//h2[@class='col-sm-6 h3']")

