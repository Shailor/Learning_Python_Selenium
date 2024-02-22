import pytest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

"""
Test plan:
1. Test that page is accessable 
2. Test that Element A can be dragged and dropped to element B
"""

@pytest.fixture(scope="function", autouse=True)
def test_setup(driver,baseurl):
    test_url = baseurl + "drag_and_drop"
    driver.get(test_url)
    

def test_website_acessable(driver):
    assert "Drag and Drop" in driver.page_source
    
def test_drag_A_to_B(driver):
    right_element = driver.find_element(By.XPATH, '//*[@id="column-a"]')
    left_element = driver.find_element(By.XPATH, '//*[@id="column-b"]')
    
    assert right_element.text == "A" and left_element.text == "B"   
    
    drag_and_drop = ActionChains(driver).drag_and_drop
    
    drag_and_drop(right_element,left_element).perform()
    
    right_element = driver.find_element(By.XPATH, '//*[@id="column-a"]')
    left_element = driver.find_element(By.XPATH, '//*[@id="column-b"]')
    
    assert right_element.text == "B" and left_element.text == "A"
    