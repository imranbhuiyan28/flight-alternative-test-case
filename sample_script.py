from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

sleep(2)

driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.CSS_SELECTOR, "[data-test = '@web/Search/SearchButton' ]" ).click()
sleep(2)


url = driver.current_url
print(url)
# expect = 'tea'
# actual = driver.find_element(By.XPATH, "//div[@data-module-type = 'ListingPageResultsCount']").text
# print(actual, expect)
# # assert expect == actual , f""
#
expect = 'tea'
assert expect in url, f"{url} does not match the expected value"
title = driver.title
print(title)
print(f"url: {url} and test passed ")
print("test passed")

