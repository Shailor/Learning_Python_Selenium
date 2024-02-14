from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pytest



class TestAddRemoveElements:
    def setup_method(self, method):

        self.browser = webdriver.Chrome()
        self.browser.get("http://localhost:7080/add_remove_elements/")
        self.browser.implicitly_wait(1)
    
    def teardown_method(self, method):
        self.browser.close()
        
        
    def test_add_element(self):
        add_elements = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/button')
        
        num_of_elements = 2
        
        for i in range(num_of_elements):
            add_elements.click()
        
        elements = self.browser.find_elements(By.XPATH, '//*[@id="elements"]/button')
        assert len(elements) == num_of_elements
        
    
    def test_delete_element(self):
        add_elements = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/button')
        num_of_elements = 2
        for _ in range(num_of_elements):
            add_elements.click()
        
        elements = self.browser.find_elements(By.XPATH, '//*[@id="elements"]/button')
        assert len(elements) == num_of_elements
        
        for _ in range(num_of_elements):
            elements[0].click()
            num_of_elements = num_of_elements - 1 
            elements = self.browser.find_elements(By.XPATH, '//*[@id="elements"]/button')
            assert len(elements) == num_of_elements
        
