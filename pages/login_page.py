from .base_page import BasePage
from selenium import webdriver
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_currect_login_url(self):
        driver = webdriver.Chrome()
        driver.get("http://selenium1py.pythonanywhere.com/es/accounts/login/")
        assert "login" in driver.current_url, "Wrong login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"
