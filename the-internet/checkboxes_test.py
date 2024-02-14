from selenium import webdriver
from selenium.webdriver.common.by import By




class TestCheckboxes:
    def setup_method(self, method):
        
        self.browser = webdriver.Chrome()
        self.browser.get("http://localhost:7080/checkboxes")
        self.browser.implicitly_wait(5)
        self.elements = self.browser.find_elements(By.XPATH, '//*[@id="checkboxes"]/input')
    
    def teardown_method(self, method):
        self.browser.close()
        
    def test_check_number_of_checkboxes(self):
        assert len(self.elements) == 2
        
        
    def test_check_checkbox1(self):
        assert self.elements[0].is_selected() == False
        self.elements[0].click()
        assert self.elements[0].is_selected() == True
        
        
    def test_uncheck_checkbox(self):
        assert len(self.elements) == 2
        assert self.elements[1].is_selected() == True
        self.elements[1].click()
        assert self.elements[1].is_selected() == False
        