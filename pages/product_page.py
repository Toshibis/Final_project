from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def check_name_and_price_of_product(self):
        title_name = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_NAME)
        book_title_name = title_name.text
        name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name = name.text
        if book_title_name == book_name:
            print("The book name is correct")
        else:
            print("The book name wrong")
        assert {book_title_name} == {book_name}, "BUG - name wrong"
        title_price = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_PRICE)
        book_title_price = title_price.text
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price = price.text
        if book_title_price == book_price:
            print("The price is correct")
        else:
            print("The price wrong")
        assert {book_title_price} == {book_price}, "BUG - price wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Not disappeared"
