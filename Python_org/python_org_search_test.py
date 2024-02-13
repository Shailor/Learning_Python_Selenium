import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestPythonOrgSearch():
    def setup_method(self, method):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.python.org")
        self.browser.implicitly_wait(5)


    def teardown_method(self, method):
        self.browser.close()
    

    def test_python_org_is_accessable(self):
        assert "Python" in self.browser.title
    

    def test_python_org_search(self):
        elem = self.browser.find_element(By.NAME, "q")
        elem.clear()  # clear element's prefilled information
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        
        assert "No results found" not in self.browser.page_source
        
        search_results = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul')
        assert "PyCon" in search_results.text

    def test_python_org_serch_invalid_data(self):
        elem = self.browser.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("asdfasdf")
        elem.send_keys(Keys.RETURN)
        
        
        assert "No results found" in self.browser.page_source
        