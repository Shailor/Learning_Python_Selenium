from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from conftest import close_ads

def test_product_search(driver):
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
    
    
    retry_counter = 0
    while retry_counter < 3:
        try:
            driver.find_element(By.XPATH, '//*[@id="search_product"]').send_keys('shirt')
            driver.find_element(By.XPATH, '//*[@id="submit_search"]').click()
            assert 'Searched Products' in driver.page_source
            break
        except:
            close_ads(driver)
            retry_counter += 1
    
    
    products = driver.find_elements(By.CLASS_NAME, 'single-products')
    assert len(products) > 0


def test_search_unexisting_item(driver):
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
    
    
    retry_counter = 0
    while retry_counter < 3:
        try:
            driver.find_element(By.XPATH, '//*[@id="search_product"]').send_keys('asdfasdfa')
            driver.find_element(By.XPATH, '//*[@id="submit_search"]').click()
            assert 'Searched Products' in driver.page_source
            break
        except:
            close_ads(driver)
            retry_counter += 1
    

    
    products = driver.find_elements(By.CLASS_NAME, 'single-products')
    
    
    assert len(products) == 0
