from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



IMG = (By.CSS_SELECTOR, "[alt='Website for automation practice']")
TXT = (By.XPATH, "//b[text()= 'Enter Account Information']")
USER_EXIST = (By.XPATH, "//p[contains(text(),'Email Address already exist!')]")
CONTACT_TXT = (By.XPATH, "//h2[contains(text(),'Contact ')]")
SUCCESS_VERIFY_TXT = (By.CSS_SELECTOR, "[class='status alert alert-success']")
ALL_PRODUCT = (By.XPATH, "//h2[contains(text(),'All Products')]")
PRODUCT_INFO = (By.CSS_SELECTOR, "[class='product-information']")

@then('Verify that home page is visible successfully')
def verify_home_page_is_visible(context):
    wait = WebDriverWait(context.driver, 10)
    img = wait.until(EC.visibility_of_element_located(IMG))
    if img.is_displayed():
        print("Home page is visible. Verify that home page is visible successfully")
    else:
        print("Home page is NOT visible")




@when('Verify New User Signup! is visible')
def verify_new_user_signup(context):
    wait = WebDriverWait(context.driver, 10)
    url = context.driver.current_url
    print(url)
    expect = 'login'
    assert expect in url, f"verify new user signup page in  {url} failed"
    print("Verify new user signup page passed")


@when("Verify that ENTER ACCOUNT INFORMATION is visible")
def verify_account_information(context):
    # expected_text = "Enter Account Information"
    # actual_text = context.driver.find_element(*TXT).text
    context.app.base_page.verify_text('ENTER ACCOUNT INFORMATION', *TXT)

@when ("Verify error Email Address already exist is visible")
def verify_email_address_already_exists(context):
    context.app.base_page.verify_text('Email Address already exist!', *USER_EXIST)


@then ("Verify GET IN TOUCH is visible")
def verify_touch(context):
    expected = "contact"
    actual_text = context.driver.find_element(*CONTACT_TXT).text.lower()
    assert expected in actual_text, f"verify touch page in '{actual_text}' failed"


@then ("Verify success message is visible")
def verify_success(context):
    expect_text = "Success! Your details have been submitted successfully."
    actual_text = context.driver.find_element(*SUCCESS_VERIFY_TXT).text
    assert expect_text in actual_text, f"verify success page in '{actual_text}' failed"


@when ("Verify user is navigated to ALL PRODUCTS page successfully")
def verify_all_products(context):
    expected_text = "ALL PRODUCTS"
    actual_text = context.driver.find_element(*ALL_PRODUCT).text
    assert expected_text in actual_text, f"verify all products page in '{actual_text}' failed"


@when ("Verify that detail")
def verify_detail(context):
    info = context.driver.find_element(*PRODUCT_INFO).text
    print(info)
    assert info , f"verify detail page in '{info}' failed"
    print("Verify detail page passed")


@then("Verify SUBSCRIPTION is visible")
def verify_subscription(context):
    expected = "SUBSCRIPTION"
    actual_text = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Subscription')]").text
    print(actual_text)
    assert expected == actual_text, f"verify subscription page in '{actual_text}' failed"


@then ("Verify that page is scrolled up and Full-Fledged practice website for Automation text is visible on screen")
def verify_full_fledged_practice_website(context):
    expected = 'Full-Fledged practice website for Automation Engineers'
    actual_text = context.driver.find_element(By.XPATH,"//h2[contains(text(),'Full-Fledged practice website for Automation Engineers')]").text
    print(actual_text)
    assert actual_text in expected, f"test failed"


LOGIN_TXT = (By.XPATH, "//h2[contains(text(),'Login to your account')]")
LOGGED_IN = (By.XPATH,"//*[contains(text(), 'Logged in as')]")
CART_QTY_TEXT = (By.CSS_SELECTOR, "td.cart_quantity > button")



@then ("Verify Login to your account is visible")
def verify_login(context):
    expected = "Login"
    actual_text = context.driver.find_element(*LOGIN_TXT).text
    print(actual_text)
    assert expected in actual_text, f"verify login page in '{actual_text}' failed"
    print("Verify login page passed")





@when("Verify that Logged in  is visible")
def verify_logged_in(context):
    expected = "cooper"
    actual = context.driver.find_element(*LOGGED_IN).text
    print(actual)
    assert expected in actual, f"verify logged in page in '{actual}' failed"




@then ("Verify navigate to Login to your account page")
def verify_navigate(context):
    expected = "Login"
    actual_text = context.driver.find_element(*LOGIN_TXT).text
    print(actual_text)
    assert expected in actual_text, f"verify login page in '{actual_text}' failed"
    print("Verify login page passed")


@then ("Verify that product is displayed in cart page with exact quantity")
def verify_cart_product(context):
    check_out = context.driver.find_element(*CART_QTY_TEXT)
    actual_qty = check_out.text.strip()
    print(f"Checkout quantity: {actual_qty}")
    assert actual_qty == '4', f"Expected quantity '{check_out}', but got '{actual_qty}'"


















