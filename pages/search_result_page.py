

from pages.base_page import BasePage


from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys



class SearchResultPage(BasePage):

    #all locator for verifying text
    LINK = (By.CSS_SELECTOR, "[data-test = '@web/slingshot-components/CellsComponent/Link']")
    CART_VERIFY = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    ITEM_VERIFY = (By.XPATH, "//span[contains(text(), 'subtotal')]")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    TITLE = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    VERIFY_FSV_TEXT = (By.XPATH, "//div[contains(text(),'Click to sign in and save')]")

    def verify_url(self,product):
            self.verify_partial_url(product)



    def verify_block(self, number):
        cells = self.driver.find_elements(*self.LINK)
        print(len(cells))
        if len(cells) >= int(number):
            print("test passed")

        else:
            print("ERROR")
            assert False, f"Expected {number} cells, but found {len(cells)}"




    def verify_cart_text(self):
        expected_text = "Your cart is empty"
        # actual_text = self.driver.find_element(*self.CART_VERIFY).text
        # assert expected_text == actual_text, f"Expected {expected_text}, but found {actual_text}"
        self.verify_text(expected_text, *self.CART_VERIFY)


    def verify_item(self,amount):

        actual_text = self.driver.find_element(*self.ITEM_VERIFY).text
        print(actual_text)

        assert f'{amount} item' in actual_text , f'not passed'
        sleep(5)




    def verify_product_title(self,expected_text):
        self.verify_text(expected_text, *self.PRODUCT_TITLE)
        print(expected_text)



    def hove_icon_shown(self):
        self.wait_for_element_visible(*self.VERIFY_FSV_TEXT)







