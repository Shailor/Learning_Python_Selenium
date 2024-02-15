from selenium import webdriver

import pytest


@pytest.fixture
def baseurl():
    return "http://localhost:7080/"
    # return "https://the-internet.herokuapp.com/"

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    yield browser
    browser.close()