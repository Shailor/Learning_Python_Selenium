import pytest

from selenium.webdriver.common.by import By

import requests



"""
Test plan
1. Test that you can access page
2. Test that there are pictures and they are accessable (not broken)
3. Test that text is present
4. Update the page and check that the contents have changed
"""


@pytest.fixture(scope='function', autouse=True)
def test_setup(driver, baseurl):
    test_url = baseurl + "dynamic_content"
    driver.get(test_url)
    yield {"test_url": test_url}
    
def test_webpage_acessable(driver):
    assert "Dynamic Content" in driver.page_source 


def get_picture_src(driver):
    pictures = driver.find_elements(By.XPATH, '//*[@id="content"]/div[.]/div[.]/img')
    src = list()
    for i in range(len(pictures)):
        src.append(pictures[i].get_attribute('src'))  
    for i in range(len(src)):
        r = requests.get(src[i])
        assert r.status_code == 200
        
    return src
    
    
def test_pictures_change_after_refresh(driver):
    src = get_picture_src(driver)
    driver.refresh()
    src2 = get_picture_src(driver)
    assert src2 != src
    

def test_text(driver):
    text = driver.find_elements(By.XPATH, '//*[@id="content"]/div[.]/div[2]')
    for i in range(len(text)):
        assert text[i].text != None
    driver.refresh()
    text2 = driver.find_elements(By.XPATH, '//*[@id="content"]/div[.]/div[2]')
    assert len(text) == len(text2)
    for i in range(len(text)):
        assert text[i] != text2[i]
        
