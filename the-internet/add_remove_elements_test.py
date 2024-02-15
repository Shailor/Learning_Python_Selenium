from selenium.webdriver.common.by import By

import pytest


@pytest.fixture(scope="function",autouse=True)
def test_setup(driver, baseurl):
    driver.get(baseurl + "add_remove_elements/")

        
        
def test_add_element(driver):
    add_elements = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
    
    num_of_elements = 2
    
    for i in range(num_of_elements):
        add_elements.click()
    
    elements = driver.find_elements(By.XPATH, '//*[@id="elements"]/button')
    assert len(elements) == num_of_elements
    

def test_delete_element(driver):
    add_elements = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
    num_of_elements = 2
    for _ in range(num_of_elements):
        add_elements.click()
    
    elements = driver.find_elements(By.XPATH, '//*[@id="elements"]/button')
    assert len(elements) == num_of_elements
    
    for _ in range(num_of_elements):
        elements[0].click()
        num_of_elements = num_of_elements - 1 
        elements = driver.find_elements(By.XPATH, '//*[@id="elements"]/button')
        assert len(elements) == num_of_elements
    
