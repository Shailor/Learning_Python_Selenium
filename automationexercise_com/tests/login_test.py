import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from conftest import login, delete_user, close_ads

def test_login(driver, login_info):
    login(driver, login_info)
    assert "Logged in as " + login_info.get('name') in driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a').text
    
    retry_counter = 0
    while(retry_counter < 3):
        try:
            delete_user(driver)
            assert 'Account Deleted!' in driver.page_source
            break
        except:
            close_ads(driver)
            retry_counter += 1
            
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
    assert 'Automation Exercise' in driver.title