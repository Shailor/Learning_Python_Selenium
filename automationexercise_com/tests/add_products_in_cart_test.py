from selenium.webdriver.common.by import By
import re
from conftest import close_ads

def get_price_number(WebElement):
    for i in range(len(WebElement)):
        WebElement[i] = (int(re.findall(r'\d+', WebElement[i].text)[0]))

    return WebElement

def test_products_page(driver):
    assert "Automation Exercise" in driver.title
    
    retry_counter = 0
    while retry_counter < 3:
        try:
            # navigate to products page
            driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a').click()
            assert driver.current_url == 'https://automationexercise.com/products'
            break
        except:
            close_ads(driver)
            retry_counter += 1
    
    
    # find Add to cart buttons
    add_item_to_cart = driver.find_elements(By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[.]/div/div[1]/div[1]/a')
    price_of_item = driver.find_elements(By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[.]/div/div[1]/div[1]/h2')

    # get the price of items
    price_of_item = get_price_number(price_of_item)
    
    # add 1st product to the cart
    add_item_to_cart[0].click()
    # click continue shopping
    driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button').click()
    # add 2nd product to the cart
    add_item_to_cart[1].click()
    # click View Cart
    driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a').click()
    
    cart_items = driver.find_elements(By.XPATH, '/html/body/section/div/div[2]/table/tbody/tr[.]')
    assert len(cart_items) == 2
    
    
    # assert quantity
    item_quantity = driver.find_elements(By.XPATH, ' /html/body/section/div/div[2]/table/tbody/tr[.]/td[4]/button')
    for i in range(len(item_quantity)):
        item_quantity[i] = int(item_quantity[i].text)

    for i in item_quantity:
        assert i == 1
    
    # assert price of items:
    total_price = driver.find_elements(By.XPATH, '/html/body/section/div/div[2]/table/tbody/tr[.]/td[5]/p')
    total_price = get_price_number(total_price)
    for i in range(len(cart_items)):
        assert total_price[i] == price_of_item[i] * item_quantity[i]
    