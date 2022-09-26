from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_opened_from_main_page(self):
        basket_opened = self.browser.find_element(*MainPageLocators.BASKET_LINK_MP)
        basket_opened.click()
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_PRODUCT), \
            "Product is presents in basket, but should not be"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "The basket not empty"

    def basket_opened_from_product_page(self):
        basket_opened = self.browser.find_element(*ProductPageLocators.BASKET_LINK_PP)
        basket_opened.click()
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_PRODUCT), \
            "Product is presents in basket, but should not be"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "The basket not empty"
