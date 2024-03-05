from selenium.webdriver.common.by import By

from conftest import close_ads


def test_subscription(driver, login_info):
    assert "Automation Exercise" in driver.title
    
    driver.find_element(By.XPATH,'//*[@id="susbscribe_email"]').send_keys(login_info.get('email'))
    
    driver.find_element(By.XPATH, '//*[@id="subscribe"]').click()
    
    assert 'You have been successfully subscribed!' in driver.page_source