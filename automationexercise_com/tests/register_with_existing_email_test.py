import pytest


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_register_user_with_existing_email(driver, login_info_permanent_user):
    
    assert 'Automation Exercise' in driver.title
    # Get to login page
    login_info = login_info_permanent_user
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
    
    assert driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/h2').text == 'New User Signup!'
    
    # Enter name
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys(login_info.get('name'))
    # Enter email
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys(login_info.get('email'))
    # click on signup button
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()
    
    assert 'Email Address already exist!' in driver.page_source