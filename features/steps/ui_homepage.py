from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HAMBURGER = (By.CSS_SELECTOR, "[class='navbar-toggler-icon']")
HOTEL_BTN = (By.XPATH, "//a[contains(text(), 'Hotels')]")
HOTEL_TXT = (By.XPATH, "//strong[contains(text(), 'Featured Hotels')]")

@then("all elements should align properly without horizontal scroll")
def align_properly_with_horizontal_scroll(context):
    viewport_width = context.driver.execute_script("return window.innerWidth;")
    scroll_width = context.driver.execute_script("return document.body.scrollWidth;")
    assert scroll_width <= viewport_width, (
        f"Horizontal scroll detected: page width {scroll_width}px is wider than viewport {viewport_width}px"
    )
    print(f"Viewport width: {viewport_width}px, Page width: {scroll_width}px")


@then ("the menu should collapse into a hamburger icon")
def collapse_into_hamburger_icon(context):
    hamburger = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(HAMBURGER))
    assert hamburger.is_displayed(), f"Hamburger icon not displayed: {hamburger}"


@then("the layout should not overflow or break")
def layout_should_not_overflow(context):
    viewport_width = context.driver.execute_script("return window.innerWidth;")
    scroll_width = context.driver.execute_script("return document.body.scrollWidth;")
    print(f"Viewport width: {viewport_width}px, Page width: {scroll_width}px")
    assert scroll_width <= viewport_width, (f"Layout overflow detected: page width {scroll_width}px is wider than viewport "
                                            f"{viewport_width}px")


