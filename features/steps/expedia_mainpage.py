from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

DEPART_FROM = (By.ID, 'destination_form_field')
@given("open expedia main page")
def open_expedia_main_page(context):
    context.driver.get("https://expedia.com")
    depart= context.driver.find_element(By.CSS_SELECTOR,  "[data-stid='destination_form_field-menu-trigger']")
    depart.click()
    sleep(4)

    depart_from = context.driver.wait.until(EC.presence_of_element_located(DEPART_FROM))
    depart_from.send_keys('NewYork')

    depart_from.send_keys(Keys.RETURN)


