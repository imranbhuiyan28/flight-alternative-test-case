from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class CartPage(BasePage):
    ADD_BTN = (By.CSS_SELECTOR, "[data-test = 'chooseOptionsButton']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [data-test='orderPickupButton']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    TITLE = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    FAVOURITE_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")


    def click_cart(self):
        self.click(*self.ADD_BTN)
        sleep(5)

    def cart_btn(self):
        self.click(*self.CART_BTN)


    def product_name(self):
        return self.driver.find_element(*self.TITLE).text



    def side_nav_cart(self):
        self.click(*self.PRODUCT_NAME)
        sleep(5)
        self.driver.back()
        sleep(5)
        self.wait_for_element_clickable(*self.CART_BTN)

    def click_add_cart(self):
        self.click(*self.CART_BTN)
        sleep(5)




    def hover_fav_icon(self):
        self.hover_element(*self.FAVOURITE_ICON)
        sleep(5)














