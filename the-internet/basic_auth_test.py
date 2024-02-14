from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import ait

import pytest

class TestBasicAuth:
    
    def setup_method(self, method):
        chrome_options = Options()
        
        chrome_options.add_experimental_option("detach", False)
        self.browser = webdriver.Chrome(chrome_options)
        
        self.browser.implicitly_wait(5)
        self.wait = WebDriverWait(self.browser, 10)
        
    def teardown_method(self, method):
        self.browser.close()
        

    def test_valid_credentials_in_url(self):
        self.browser.get("http://admin:admin@localhost:7080/basic_auth")
        assert "Congratulations! You must have the proper credentials." in self.browser.page_source
        
    def test_valid_credentials_input(self):
        self.browser.get("http://localhost:7080/basic_auth")
        
        for _ in range (2):
            ait.write("admin")
            ait.press('tab')
        
        ait.press('enter')
        
        self.wait.until(EC.presence_of_element_located((By.ID, "content")))
        assert "Congratulations! You must have the proper credentials." in self.browser.page_source
        
    def test_invalid_credentials(self):
        self.browser.get("http://localhost:7080/basic_auth")
        
        for _ in range(3):
            ait.press('tab')
        
        ait.press('enter')
        
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        assert "Not authorized" in self.browser.page_source
    