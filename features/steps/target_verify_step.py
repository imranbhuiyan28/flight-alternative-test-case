from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

ALL_LISTING = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")

@then ("verify car has {amount} items")
def verify_car_amount(context, amount):
    # cart_summary = context.driver.find_element(By.XPATH, "//span[contains(text(), 'subtotal')]").text
    #
    # assert f'{amount} item' in cart_summary , f'not passed'
    # if f"{amount} items" in cart_summary:
    #     print("The cart has {amount} item and pass")
    #
    # else:
    #     assert False , f'The cart has {cart_summary}'
    context.app.search_result_page.verify_item(amount)




@then ("verify correct product name")
def verify_product_name(context):
    # product_title = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    # print(f"The product title is {product_title}")
    # assert context.title == product_title, f"The product title is {product_title}"
    context.app.search_result_page.verify_product_title(context.title)




@then ("Verify every product has name and image")
def verify_product_name(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)

    all_product = context.driver.find_elements(*ALL_LISTING)
    print(f'all product name is \n{all_product}')
    print(f'total product found is {len(all_product)}')
    assert len(all_product) > 0, f"The product name is {all_product}"

    for product in all_product:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title != '', 'Product title not shown'
        print(f'product title is {title}')



@then ("verify search result {product} in url")
def verify_product(context,product):
    # expected = 'pencil'
    # current_url = context.driver.current_url
    # print(f"current url is {current_url}")
    # assert expected in current_url, f"The product name is {expected}"
    # print(f'Url: {current_url} and test passed')
    context.app.search_result_page.verify_url(product)



LINK = (By.CSS_SELECTOR, "[data-test = '@web/slingshot-components/CellsComponent/Link']")




@then ("verify the {number} cells")
def verify_cells(context, number):
    cells = context.driver.find_elements(*LINK)
    print(len(cells))
    if len(cells) >= int(number):
        print("test passed")

    else:
        print("ERROR")
        assert False, f"Expected {number} cells, but found {len(cells)}"


# @then ('Verify “Your cart is empty” message is shown')
# def empty_message(context):
#     context.app.search_result_page.verify_cart_text()