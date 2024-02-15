import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function", autouse=True)
def test_setup(driver):
    driver.get("https://www.python.org")



def test_python_org_is_accessable(driver):
    assert "Python" in driver.title


def test_python_org_search(driver):
    elem = driver.find_element(By.NAME, "q")
    elem.clear()  # clear element's prefilled information
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)

    search_results = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul')
    assert "PyCon" in search_results.text

def test_python_org_serch_invalid_data(driver):
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("asdfasdf")
    elem.send_keys(Keys.RETURN)
    
    search_results = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul')
    assert "No results found" in search_results.text
    