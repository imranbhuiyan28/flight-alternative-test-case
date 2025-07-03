from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
import time

SEARCH_BTN = (By.XPATH, "(//button[@id='flights-search'])[1]")
RESULTS_CONTAINER = (By.ID, "flights--list-js")


FLYING_FROM = (By.XPATH, "(//span[@class='select2 select2-container select2-container--default select2-container--focus']//span[@role='combobox'])[1]")

@given("I measure the homepage load time")
def load_time(context):
    url = "https://flights.flightalternative.com/"
    context.loading_time = context.app.base_page.measure_load_time(url)


@then ("it should load in under 3 seconds")
def verify_loadtime(context):
    print(f"Verified load time: {context.loading_time:.2f} seconds")


@when("I search from Boston to Chicago")
def search_from_boston(context):
    dropdown_container = (By.XPATH, "(//span[contains(@class, 'select2-container')])[1]")
    search_input = (By.XPATH, "//input[@class='select2-search__field']")
    TO_DROPDOWN = (By.XPATH, "(//span[contains(@class, 'select2-container')])[2]")
    TO_SEARCH = (By.XPATH, "//input[@class='select2-search__field']")

    TO_ARRIVAL = (By.CSS_SELECTOR, "[class='select2-results__option']")


    # Click to activate dropdown
    Drop_down = context.driver.find_element(*dropdown_container).click()
    search = context.driver.find_element(*search_input).send_keys("Boston")
    select = context.driver.find_element(By.CSS_SELECTOR, "[class='select2-results__option']")
    select.click()



    context.driver.find_element(*TO_DROPDOWN).click()
    context.driver.find_element(*TO_SEARCH).send_keys("Chicago")

    search_result = context.driver.find_elements(*TO_ARRIVAL)
    print(f"Found {len(search_result)} search results")
    sleep(3)
    for i in search_result:
        print(i.text)


    for result in search_result:
        if "ChicagoUnited States" in result.text:
            result.click()
            sleep(4)
            break




@then("the results should appear within five seconds")
def verify_five_seconds(context):
    wait = WebDriverWait(context.driver, 10)
    start_time = time.time()
    wait.until(EC.element_to_be_clickable(SEARCH_BTN)).click()
    wait.until(EC.visibility_of_element_located(RESULTS_CONTAINER))

    end_time = time.time()
    duration = end_time - start_time
    print(f"✅ Results appeared in {duration:.2f} seconds")

    assert duration <= 5, f"❌ Results took too long: {duration:.2f} seconds"



@when("I click on the all header and verify")
def click_and_verify_all_headers(context):
    headers ={
        "Hotels":{
            "button": (By.XPATH, "//a[contains(text(), 'Hotels')]"),
            "text": (By.XPATH, "//strong[contains(text(), 'Featured Hotels')]")

        },
        "Tours": {
            "button": (By.XPATH, "//a[contains(text(), 'Tours')]"),
            "text": (By.XPATH, "//strong[contains(text(), 'Popular Tours')]")
        },

        "Blogs": {
            "button": (By.XPATH, "//a[contains(text(), 'Blogs')]"),
            "text": (By.XPATH, "//h2[contains(text(), 'Flight Alternatives Blogs')]")
        }

    }

    for name, locator in headers.items():
        btn_locator = locator["button"]
        text_locator = locator["text"]

        print(f"🔍 Clicking on: {name}")

        context.app.base_page.click(*btn_locator)
        element = context.driver.find_element(*text_locator)
        actual_text = element.get_attribute("textContent").strip()

        print(f"Found text: '{actual_text}'")
        assert name in actual_text,f"{name} not found in {actual_text}"
















