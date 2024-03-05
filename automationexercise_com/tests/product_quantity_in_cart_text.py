from selenium.webdriver.common.by import By
import re

from conftest import get_price_number


def test_product_quantity_in_cart(driver):
    assert "Automation Exercise" in driver.title
    
    # click on product details
    driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a').click()
    
    assert 'https://automationexercise.com/product_details/' in driver.current_url
    
    price = get_price_number(driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span'))
    
    # change quantity
    quantity = '4'
    driver.find_element(By.XPATH, '//*[@id="quantity"]').send_keys(quantity)
    
    # add to cart
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button').click()
    
    # go to cart
    driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a').click()
    
    
    # TODO finish this 
    