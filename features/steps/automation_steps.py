from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


IMG = (By.CSS_SELECTOR, "[alt='Website for automation practice']")
LOGIN_SIGNUP_BTN = (By.XPATH, "//a[@href = '/login']")
NAME = (By.CSS_SELECTOR, "form[action='/signup'] input[name='name']")
EMAIL = (By.CSS_SELECTOR, "form[action='/signup'] input[name='email']")
SIGNUP_BTN = (By.CSS_SELECTOR, "[data-qa='signup-button']")
TXT = (By.XPATH, "//b[text()= 'Enter Account Information']")
RADIO_BTN = (By.ID, 'id_gender1')
PASSWORD = (By.CSS_SELECTOR, "[type='password']")
DOF_DAY = (By.CSS_SELECTOR, "[id='days']")
DOF_MONTH = (By.CSS_SELECTOR, "[id='months']")
DOF_YEAR = (By.CSS_SELECTOR, "[id='years']")
NEWS_LETTER = (By.ID, "newsletter")
OFFER = (By.ID, "optin")
FIRST_NAME = (By.ID, "first_name")
LAST_NAME = (By.ID, "last_name")
COMPANY_NAME = (By.ID, "company")
ADDRESS1 = (By.ID, "address1")
STATE = (By.ID, "state")
CITY = (By.ID, "city")
ZIPCODE = (By.ID, "zipcode")
MOBILE = (By.ID, "mobile_number")
CREATE_ACCOUNT = (By.CSS_SELECTOR, "[data-qa='create-account']")
COUNTRY = (By.ID, "country")
ACC_CREATE_TEXT = (By.XPATH, "//p[contains(text(),'Congratulations! Your new account has been success')]")
CONT_BTN = (By.CSS_SELECTOR, "[data-qa='continue-button']")
USER_NAME = (By.XPATH, "//a[contains(text(), 'Logged in as')]")
DELETE_BTN = (By.CSS_SELECTOR, "a[href='/delete_account']")
DELETE_TXT = (By.XPATH, "//h2[contains(text(), 'ACCOUNT DELETED')]")
DEL_BTN = (By.XPATH, "//a[contains(text(),'Delete Account')]")
CONTACT_US = (By.CSS_SELECTOR, "[class='fa fa-envelope']")
CONTACT_US_NAME = (By.NAME, "name")
CONTACT_US_email = (By.NAME, "email")
CONTACT_US_SUBJECT = (By.NAME, "subject")
CONTACT_US_MESSAGE = (By.NAME, "message")
UPLOAD = (By.NAME, "upload_file")
SUBMIT = (By.NAME, "submit")
PRODUCT = (By.XPATH, "//a[@href = '/products']")
PRODUCT_LIST = (By.CSS_SELECTOR,"[class='fa fa-plus-square']")
ADD_CART = (By.CSS_SELECTOR, "[data-product-id='1']")









@given("Open the main page")
def open_main_page(context):
    context.app.main_page.open_automation_website()



@then ('Click on Signup / Login button')
def click_signup(context):
    context.app.base_page.click(*LOGIN_SIGNUP_BTN)
    sleep(5)

@when("Enter name and email address")
def enter_name(context):
    context.app.base_page.input_text('cooper', *NAME )
    context.app.base_page.input_text('cooper101@gmail.com', *EMAIL)
    sleep(2)
    context.app.base_page.click(*SIGNUP_BTN)
    sleep(5)

@then("Fill details: Title, Name, Email, Password, Date of birth")
def fill_details(context):
    context.app.base_page.click(*RADIO_BTN)
    context.app.base_page.input_text('12345cooper', *PASSWORD)
    dd_day = context.driver.find_element(*DOF_DAY)
    dd_month = context.driver.find_element(*DOF_MONTH)
    dd_year = context.driver.find_element(*DOF_YEAR)
    select_day = Select(dd_day)
    select_month = Select(dd_month)
    select_year = Select(dd_year)

    select_day.select_by_value('18')
    select_month.select_by_visible_text('May')
    select_year.select_by_value('1995')
    sleep(2)

@when("Select checkbox Sign up for our newsletter")
def select_checkbox(context):
    context.app.base_page.click(*NEWS_LETTER)

@then("Select checkbox offer")
def select_special_offers(context):
    context.app.base_page.click(*OFFER)


@then ("Fill the address information")
def fill_address_information(context):
    context.app.base_page.input_text('cooper', *FIRST_NAME)
    context.app.base_page.input_text('Mark', *LAST_NAME)
    context.app.base_page.input_text('Automation', *COMPANY_NAME)
    context.app.base_page.input_text('455 central st', *ADDRESS1)
    dd_country = context.driver.find_element(*COUNTRY)
    select = Select(dd_country)
    select.select_by_visible_text('United States')
    sleep(2)
    context.app.base_page.input_text('Florida', *STATE)
    context.app.base_page.input_text('Miami', *CITY)
    context.app.base_page.input_text('11234', *ZIPCODE)
    context.app.base_page.input_text('347-450-7879', *MOBILE)
    context.app.base_page.click(*CREATE_ACCOUNT)
    sleep(2)



@then("Verify that ACCOUNT CREATED is visible")
def verify_account_created_visible(context):
    context.app.base_page.verify_text('Congratulations! Your new account has been successfully created!', *ACC_CREATE_TEXT)





@then ("Click on Contact Us button")
def click_contact_us(context):
    context.app.base_page.click(*CONTACT_US)


@when ("Enter information and message")
def enter_info(context):
    context.app.base_page.input_text('cooper', *CONTACT_US_NAME)
    context.app.base_page.input_text('cooper101@gmail.com', *CONTACT_US_email)
    sleep(2)
    context.app.base_page.input_text('Automation in test', *CONTACT_US_SUBJECT)
    context.app.base_page.input_text('This is a test from qa ', *CONTACT_US_MESSAGE)
    sleep(2)
    # screen = context.driver.save_screenshot("upload.png")

@then ("Upload file")
def upload_file(context):
    upload = context.driver.find_element(*UPLOAD)
    upload.send_keys("C:\\Users\\ibhui\\Desktop\\python-selenium-automation\\upload.png")
    sleep(2)

@then ("Click Submit button")
def click_submit(context):
    context.app.base_page.click(*SUBMIT)
    sleep(2)

@then ("Click OK button")
def click_ok(context):
    popup = context.driver.switch_to.alert
    popup.accept()
    sleep(2)


@when ("Click on Products button")
def click_product(context):
    context.app.base_page.click(*PRODUCT)

@when ("Click on View Product of first product")
def click_product_first(context):
    # Remove iframes
    context.driver.execute_script("""
        document.querySelectorAll('iframe').forEach(el => el.remove());
    """)

    product_list = context.driver.find_elements(*PRODUCT_LIST)
    print(f"total product: {len(product_list)}")

    if product_list:
        # Scroll to and click using ActionChains for better reliability
        element = product_list[0]
        context.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        ActionChains(context.driver).move_to_element(element).click().perform()
    else:
        print("no product")

    sleep(2)


@then ("Hover over first product and click Add to cart")
def click_cart(context):
    add_cart = context.driver.find_element(*ADD_CART)
    action = ActionChains(context.driver)
    action.move_to_element(add_cart).perform()
    sleep(2)
    add_cart.click()
    sleep(5)

@then ("Scroll down page to bottom")
def scroll_down(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)



@when ("move upward")
def move_up(context):
    context.driver.execute_script("window.scrollTo(0, 0);")
    sleep(2)

LOGIN_EMAIL = (By.CSS_SELECTOR, "form[action='/login'] input[name='email']")
LOGIN_PASSWORD = (By.CSS_SELECTOR, "form[action='/login'] input[name='password']")
LOGIN_BTN = (By.CSS_SELECTOR, "form[action='/login'] button[type='submit']")
LOG_OUT_BTN = (By.CSS_SELECTOR, "[class='fa fa-lock']")
QTY = (By.ID, "quantity")
ADD_TO_CART = (By.CSS_SELECTOR, "[class='btn btn-default cart']")
VIEW_CART = (By.XPATH, "//u[text()='View Cart']")

@then("Enter correct email address and password")
def enter_correct_email(context):
    context.app.base_page.input_text("cooper101@gmail.com", *LOGIN_EMAIL)
    context.app.base_page.input_text("12345cooper", *LOGIN_PASSWORD)
    sleep(2)

@then("Click login button")
def click_login(context):
    context.app.base_page.click(*LOGIN_BTN)
    sleep(4)

@then("click on logout button")
def click_logout(context):
    context.app.base_page.click(*LOG_OUT_BTN)
    sleep(2)

@then("Increase quantity to 4")
def increase_quantity(context):
    qty_input = context.driver.find_element(*QTY)
    qty_input.clear()
    qty_input.send_keys(4)
    sleep(2)


@then ("Click Add to cart button")
def click_add_cart(context):
    context.app.base_page.click(*ADD_TO_CART)
    sleep(2)


@then ("Click View Cart button")
def click_view_cart(context):
    context.app.base_page.click(*VIEW_CART)
    sleep(2)


















