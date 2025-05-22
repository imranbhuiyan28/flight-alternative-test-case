from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



@given("open website pages")
def open_website_pages(context):
    context.app.main_page.open_sace_demo()