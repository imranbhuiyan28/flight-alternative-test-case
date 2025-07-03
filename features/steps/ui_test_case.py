from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


SEARCH_BTN = (By.XPATH, "//button[@id='flights-search']")

@when ("I click the Search button without filling any field")
def error_search(context):
    context.app.base_page.click(*SEARCH_BTN)
    sleep(5)