from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_currect_login_url()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_current_url(browser):
    link = "http://selenium1py.pythonanywhere.com/es/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_currect_login_url()


def test_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/es/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/es/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

# pytest -v --tb=line --language=en test_main_page.py
