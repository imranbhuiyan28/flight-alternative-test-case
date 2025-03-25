from pages.base_page import BasePage
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys





class TargetAppPage(BasePage):
    PP_LINK = (By.CSS_SELECTOR, "[aria-label='privacy policy - opens in a new window']")


    def click_privacy(self):
        self.click(*self.PP_LINK)
        sleep(2)


    def privacy_policy_verify(self):
        self.verify_partial_url('target-privacy-policy')




