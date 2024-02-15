import pytest
import requests

from selenium.webdriver.common.by import By


@pytest.fixture(scope="function", autouse=True)
def test_setup(driver, baseurl):
    url = baseurl + "broken_images"
    driver.get(url)
    images = driver.find_elements(By.XPATH, '//*[@id="content"]/div/img')
    yield {"images": images}
    
    
def test_number_of_pictures(baseurl,test_setup):
        images = test_setup.get("images")
        assert len(images) == 3

@pytest.mark.xfail(reason="broken image, incorrect status code in assert")
def test_picture_1(baseurl, test_setup):
    images = test_setup.get("images")
    src = images[0].get_attribute("src")
    r = requests.get(src)
    assert r.status_code == 200
    
def test_picture_2(baseurl, test_setup):
    images = test_setup.get("images")
    src = images[1].get_attribute("src")

    r = requests.get(src)
    assert r.status_code == 404
    
def test_picture_3(baseurl, test_setup):
    images = test_setup.get("images")
    src = images[2].get_attribute("src")

    r = requests.get(src)
    assert r.status_code == 200