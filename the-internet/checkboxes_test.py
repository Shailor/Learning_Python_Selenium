from selenium.webdriver.common.by import By

import pytest

@pytest.fixture(scope="function" ,autouse=True)
def test_setup(driver, baseurl):
    driver.get(baseurl + "checkboxes")
    

def test_check_number_of_checkboxes(driver):
    elements = driver.find_elements(By.XPATH, '//*[@id="checkboxes"]/input')
    assert len(elements) == 2
    
    
def test_check_checkbox1(driver):
    elements = driver.find_elements(By.XPATH, '//*[@id="checkboxes"]/input')
    assert elements[0].is_selected() == False
    elements[0].click()
    assert elements[0].is_selected() == True
    
    
def test_uncheck_checkbox(driver):
    elements = driver.find_elements(By.XPATH, '//*[@id="checkboxes"]/input')
    assert len(elements) == 2
    assert elements[1].is_selected() == True
    elements[1].click()
    assert elements[1].is_selected() == False
    