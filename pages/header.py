from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Header(BasePage):
    SEARCH_PRODUCT = (By.XPATH, "//input[@data-test = '@web/Search/SearchInput']")
    SEARCH_BTN = (By.XPATH, "//button[text() = 'search']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_PRODUCT)
        self.click(*self.SEARCH_BTN)
        sleep(10)





