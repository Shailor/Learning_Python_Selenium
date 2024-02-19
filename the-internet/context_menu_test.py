import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function', autouse=True)
def test_setup(driver, baseurl):
    test_url = baseurl + "context_menu"
    driver.get(test_url)    

def test_allert_triger(driver):
    element = driver.find_element(By.ID, "hot-spot")
    actionChains = ActionChains(driver)
    actionChains.context_click(element).perform()
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Allert exitst")
        alert_present = True
    except:
        print("There is no allert")
        alert_present = False

    assert alert_present == True
    
    
def test_click_wrong_place(driver):
    element = driver.find_element(By.ID, "content")
    actionChains = ActionChains(driver)
    actionChains.context_click(element).perform()
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Allert exitst")
        alert_present = True
    except:
        print("There is no allert")
        alert_present = False

        
    assert alert_present == False