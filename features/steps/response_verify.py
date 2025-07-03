from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
import time


ABOUT_US = (By.XPATH, "//a[contains(text(), 'About us')]")

@when("I click on the About footer")
def about_footer(context):
    about = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(ABOUT_US)
    )
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", about)

    # Wait until clickable
    about = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(ABOUT_US)
    )
    about.click()
    sleep(5)





