
from selenium.webdriver.common.by import By

from conftest import close_ads

def test_testcases_page(driver):
    
    assert "Automation Exercise" in driver.title
    retry_counter = 0
    while(retry_counter < 3):
        try:
            driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a').click()
            break
        except:
            close_ads(driver)
            retry_counter += 1
            
    assert driver.current_url == 'https://automationexercise.com/test_cases'
    
    