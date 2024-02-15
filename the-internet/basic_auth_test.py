
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import ait

import pytest


username = "admin"
password = "admin"

@pytest.fixture(scope="function", autouse=True)
def test_setup(driver,baseurl):
    url = baseurl + "basic_auth"
    driver.get(url)
    yield url

def test_valid_credentials_in_url(driver,test_setup):
    url = test_setup[:7] + username + ":" + password + "@" + test_setup[7:]
    driver.get(url)
    print(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "content")))
    assert "Congratulations! You must have the proper credentials." in driver.page_source
    
def test_valid_credentials_input(driver):
    
    ait.write(username)
    ait.press('tab')
    ait.write(password)
    ait.press('tab')
    ait.press('enter')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "content")))
    assert "Congratulations! You must have the proper credentials." in driver.page_source
    
def test_invalid_credentials(driver):
    for _ in range(3):
        ait.press('tab')
    
    ait.press('enter')
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    assert "Not authorized" in driver.page_source
