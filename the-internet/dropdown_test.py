import pytest

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function", autouse=True)
def test_setup(driver, baseurl):
    test_url = baseurl + "dropdown"
    driver.get(test_url)
    

def test_dropdown_link_available(driver):
    assert "Dropdown List" in driver.page_source
    
def test_select_option1(driver):
    selector = Select(driver.find_element(By.ID, "dropdown")) 
    assert selector.first_selected_option.text == "Please select an option"
    selector.select_by_visible_text("Option 1")
    assert selector.first_selected_option.text == "Option 1"
    

def test_select_option2(driver):
    selector = Select(driver.find_element(By.ID, "dropdown"))
    assert selector.first_selected_option.text == "Please select an option"
    selector.select_by_index(2)
    assert selector.first_selected_option.text == "Option 2"
