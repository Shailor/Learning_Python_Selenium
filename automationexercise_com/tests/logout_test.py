import pytest
from selenium.webdriver.common.by import By
from conftest import login


def test_logout(driver, login_info_permanent_user):
    assert 'Automation Exercise' in driver.title
    
    login(driver, login_info_permanent_user)
    
    assert "Logged in as " + login_info_permanent_user.get('name') in driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a').text
    
    # logout
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
    
    assert driver.current_url == 'https://automationexercise.com/login' 