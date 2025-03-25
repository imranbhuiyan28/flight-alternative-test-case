from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# SEARCH_PRODUCT = (By.XPATH, "//input[@data-test = '@web/Search/SearchInput']")
# SEARCH_BTN = (By.XPATH, "//button[text() = 'search']")
# ADD_BTN = (By.CSS_SELECTOR, "[data-test = 'chooseOptionsButton']")
# PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [data-test='orderPickupButton']")
BACK_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [aria-label = 'Previous' ]")
TITLE = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
PRICE = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [data-test='product-price']")
CART_BTN = (By.CSS_SELECTOR, "[data-test = '@web/CartLinkQuantity' ]")


@given ("Open target main page")
def main_page(context):
    context.app.main_page.open_main()

@given("open target circle page")
def open_target_circle(context):
    context.app.main_page.circle_target_page()


@given ('Open target app')
def open_target_app(context):
    context.app.main_page.target_app_page()


@when("Search for {product}")
def search_product(context, product):
    context.app.header.search_product(product)


@when ('Click on cart')
def click_cart(context):
    context.app.cart_page.click_cart()




@when("store product name")
def store_product_name(context):
    context.title = context.app.cart_page.product_name()
    print(f'product name : {context.title}')



@then("Confirm add to cart from side nav")
def click_from_nav_bar(context):
    # context.driver.find_element(*PRODUCT_NAME).click()
    context.app.cart_page.side_nav_cart()



@then ("Go to main page")
def cart_page(context):
    # context.driver.back()
    # context.driver.wait.until(EC.visibility_of_element_located(CART_BTN))
    context.app.cart_page.side_nav_cart()


@then ("open cart page")
def open_cart_page(context):
    # context.driver.find_element(*CART_BTN).click()
    # context.driver.wait.until(EC.element_to_be_clickable(CART_BTN))
    # sleep(2)
    context.app.cart_page.click_add_cart()


@when("Click on Cart Icon")
def click_cart_icon(context):
    context.app.cart_page.cart_btn()


@then ('Verify “Your cart is empty” message is shown')
def empty_message(context):
    context.app.search_result_page.verify_cart_text()


@when ('hover to favourite icon')
def hover_to_favourite_icon(context):
    context.app.cart_page.hover_fav_icon()

@then ('favourite icon shown')
def favourite_icon_shown(context):
    context.app.cart_page.hove_icon_shown()


#________Target app page_________________________

@given ('Store original window')
def store_original_window(context):
    context.og_window = context.app.base_page.get_current_window_handle()
    print(f'original window : {context.og_window}')


@when ('Click Privacy Policy link')
def click_privacy_policy_link(context):
    context.app.target_app_page.click_privacy()

@then ('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()


@then ('Verify Privacy Policy page opened')
def verify_privacy_policy_page_opened(context):
    context.app.target_app_page.privacy_policy_verify()

@then('Close current page')
def close_current_page(context):
    context.driver.close()


@then('Return to original window')
def return_og_windows(context):
    context.app.base_page.switch_to_windows_by_id(context.og_window)
    sleep(5)





