from selenium.webdriver.common.by import By

from conftest import close_ads

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
            
    
    # find buttons that link to the next product page
    product_list = driver.find_elements(By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[.]/div/div[2]/ul/li/a')
    
    retry_counter = 0
    while retry_counter < 3:
        try:
            product_list[0].click()
            # Check product_details page opens
            assert 'https://automationexercise.com/product_details/' in  driver.current_url
            break
        except:
            close_ads(driver)
            retry_counter += 1
    
    # assert that the product has Name
    assert driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2').text != None      
    details = ['Category:', 'Rs.', 'Availability:', 'Condition:', 'Brand:']
    for i in details:
        assert i in driver.page_source