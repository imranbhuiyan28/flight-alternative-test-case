from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

ALL_HEADERS = (By.CSS_SELECTOR, "[class = 'nav-link fadeout  waves-effect']")

@given("open website")
def open_website(context):
    context.app.main_page.open_alternative()
    sleep(4)


@then("verify {number} header")
def verify(context, number):
    all_headers = context.driver.find_elements(*ALL_HEADERS)
    print(len(all_headers))

    actual = len(all_headers)
    expected = int(number)
    print(f"Expected: {expected}, Actual: {actual}")
    assert actual == expected, f"Expected {expected} headers, but found {actual}"


