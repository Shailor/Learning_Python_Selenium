import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time
from conftest import register, delete_user, close_ads


    
def test_register_user(driver, login_info):
    
    assert 'Automation Exercise' in driver.title
    retry_counter = 0
    while retry_counter < 3:
        try:
            register(driver, login_info)
            assert "Account Created!" in driver.page_source
            break
        except:
            close_ads()
            retry_counter += 1
    
    # click continue        
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
    
    retry_counter = 0
    while(retry_counter < 3):
        try:
            driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
            assert 'Automation Exercise' in driver.title
            break
        except:
            close_ads(driver)
            retry_counter += 1
    
    assert 'Automation Exercise' in driver.title
    assert str("Logged in as " + login_info.get('name')) in driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a').text
    
    retry_counter = 0
    while(True):
        try:
            delete_user(driver)
            assert 'Account Deleted!' in driver.page_source
            break
        except:
            close_ads(driver)
            retry_counter += 1
    
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
    assert 'Automation Exercise' in driver.title