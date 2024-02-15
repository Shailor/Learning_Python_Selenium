from selenium import webdriver

import pytest


@pytest.fixture
def baseurl():
    return "http://localhost:7080/"

@pytest.fixture
def driver_setup_teardown():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.close()