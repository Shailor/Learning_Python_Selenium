import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope='function', autouse=True)
def test_setup(driver, baseurl):
    test_url = baseurl + "context_menu"
    driver.get(test_url)
    


def test_allert_triger(driver):
    element = driver.find_element(By.ID, "hot-spot")
    element.