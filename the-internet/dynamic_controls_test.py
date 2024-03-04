import pytest

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='function',autouse=True)
def test_setup(driver,baseurl):
    test_url = baseurl + 'dynamic_controls'
    driver.get(test_url)
    
    
# def test_dynamic_controls_page_accessable(driver):
#     assert "Dynamic Controls" in driver.page_source
    
@pytest.mark.skip(reason='unfinished')
def test_enable_text_box(driver):
    text_box = driver.find_element(By.XPATH, '//*[@id="input-example"]/input')
    enable_button = driver.find_element(By.XPATH, '//*[@id="input-example"]/button')
    enable_button.click()
    assert WebDriverWait(driver, 10).until(EC.element_to_be_clickable(text_box)) != False
    text_box.send_keys('Hello World')
    enable_button.click()
    assert WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(driver.find_element(By.XPATH, '//*[@id="loading"]'))) != False
    

# def test_dynamic_chackbox(driver):
#     checkbox = driver.find_element(By.ID, "checkbox")
#     button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
#     checkbox.click()
#     assert