from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




LOGO_IMG = (By.CSS_SELECTOR, "[class='logo p-1 rounded']")
NAV_BAR = (By.CSS_SELECTOR, "[class='header_menu navbar-nav']")
HERO = (By.CSS_SELECTOR, "[class='container mb-5 mt-5 search-panel']")
FOOTER = (By.CSS_SELECTOR, "[class='bg-white footer-area pt-3 aos-init aos-animate']")


@then ("an error message or warning should be displayed")
def ui_verify_error_message(context):
    try:
        WebDriverWait(context.driver, 10).until(EC.alert_is_present())
        alert = Alert(context.driver)
        print("⚠️ Alert text:", alert.text)
        alert.accept()
        print("test passed")
    except:
        assert False, "❌ Expected alert did not appear"


@then("the logo should be visible")
def ui_verify_logo_visible(context):
    logo = context.driver.find_element(*LOGO_IMG)
    assert logo.is_displayed(), f"logo is not visible"


@then ("the navigation bar should be visible")
def ui_verify_navigation_bar(context):
    navigation_bar = context.driver.find_element(*NAV_BAR)
    assert navigation_bar.is_displayed(), f"navigation bar is not visible"
    nav_items = navigation_bar.find_elements(By.TAG_NAME, "li")
    print(len(nav_items))
    print(navigation_bar.text)


@then("the hero section should be visible")
def ui_verify_hero_section(context):
    hero = context.driver.find_element(*HERO)
    assert hero.is_displayed(), "Hero section (search form area) is not visible"


@then("the footer should be visible")
def ui_verify_footer(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(FOOTER))
    footer = context.driver.find_element(*FOOTER)
    assert footer.is_displayed(), "Footer is not visible"




