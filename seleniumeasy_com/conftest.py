from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


chrome_options = Options()
chrome_options.add_experimental_option("detach",False)


@pytest.fixture
def driver():
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(2)
    yield browser
    browser.close()