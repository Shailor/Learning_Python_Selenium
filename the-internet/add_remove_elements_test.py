from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



class TestAddRemoveElements:
    def setup_method(self, method):

        self.browser = webdriver.Chrome()
        self.browser.get("http://localhost:7080/add_remove_elements/")
        self.browser.implicitly_wait(5)
    
    def teardown_method(self, method):
        self.browser.close()
        
    def test_add_element(self):
        add_elements = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/button')
        add_elements.click()
        
        elements = self.browser.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(elements) == 1
        
        add_elements.click()
        elements = self.browser.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(elements) == 2
    
    def test_delete_element(self):
        add_elements = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/button')
        add_elements.click()
        add_elements.click()
        
        elements = self.browser.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(elements) == 2
        
        
        elements[1].click()
        
        elements = self.browser.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(elements) == 1
        
        elements[0].click()
        
        elements = self.browser.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(elements) == 0
        
        