from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


# ALL LOCATOR FOR THE page
USER_NAME = (By.CSS_SELECTOR, "[data-test='username']")
PASS_WORD = (By.CSS_SELECTOR, "[data-test='password']")
LOGIN_BTN = (By.CSS_SELECTOR, "[id='login-button']")
SIDE_NAV = (By.XPATH, "//button[text()= 'Open Menu']")
LOGOUT = (By.XPATH, "//a[@id='logout_sidebar_link']")
SELECT = (By.CSS_SELECTOR, "[class='product_sort_container']")
ADD_PRODUCT = (By.CSS_SELECTOR, "[class='btn_primary btn_inventory']")
CART_ICON = (By.CSS_SELECTOR, "[class='shopping_cart_container']")
CHECK_OUT = (By.CSS_SELECTOR, "[class='btn_action checkout_button']")
FIRST_NAME = (By.CSS_SELECTOR, "[id='first-name']")
Last_name = (By.CSS_SELECTOR, "[id='last-name']")
POSTAL_CODE = (By.CSS_SELECTOR, "[id='postal-code']")
CONT = (By.CSS_SELECTOR, "[class='btn_primary cart_button']")
VERIFY = (By.XPATH, "//div[normalize-space()='SauceCard #31337']")
FINISH_BTN = (By.CSS_SELECTOR, "[class='btn_action cart_button']")


#________test started from here______________

@given ('open website page')
def open_page(context):
    context.app.main_page.open_sace_demo()


@then ('login the page')
def log_in(context):
    context.app.base_page.input_text('standard_user', *USER_NAME)
    context.app.base_page.input_text('secret_sauce', *PASS_WORD)
    sleep(1)
    context.app.base_page.click(*LOGIN_BTN)
    sleep(5)

@then('verify page open')
def verify(context):
    context.app.base_page.click(*SIDE_NAV)
    sleep(1)
    log_out = context.driver.find_element(*LOGOUT)
    assert log_out.is_displayed() , f"test failed"
    print("test passed")




@then ('sort page low to high')
def sort(context):
    dd = context.driver.find_element(*SELECT)
    sleep(2)
    select = Select(dd)
    for option in select.options:
        print(option.text)

    select.select_by_visible_text("Price (high to low)")
    sleep(1)


ALL_PRODUCT = (By.CSS_SELECTOR, "[class='inventory_item']")
@then ('pick 2 item to the cart')
def pick_two(context):

#capturing all product name and price and items in the page

    all_product = context.driver.find_elements(*ALL_PRODUCT)
    print(f"Total products available: {len(all_product)}")
    for product in all_product:
        print(product.text)
        sleep(5)
#picking two items in the cart
    product_1 = context.app.base_page.click(*ADD_PRODUCT)
    sleep(3)
    product_2 = context.app.base_page.click(*ADD_PRODUCT)
    sleep(5)

@then('click on cart icon')
def click_cart(context):
    context.app.base_page.click(*CART_ICON)
    context.app.base_page.click(*CHECK_OUT)


@when ('fill up the information')
def fill_up(context):
    context.app.base_page.input_text('Arban', *FIRST_NAME)
    context.app.base_page.input_text('Khan', *Last_name)
    context.app.base_page.input_text('12143', *POSTAL_CODE)
    sleep(3)
    context.app.base_page.click(*CONT)
    sleep(3)



@then ('verify the page')
def verify(context):
    verify_text = context.driver.find_element(*VERIFY).text
    assert verify_text == "SauceCard #31337", f"test failed"
    print("test passed")


@then  ("click finish")
def finish(context):
    context.app.base_page.click(*FINISH_BTN)









