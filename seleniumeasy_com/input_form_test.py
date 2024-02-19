import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    
    def tearDown(self):
        self.driver.close()


    def test_enter_message_field(self):
        driver = self.driver
        driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

        message_field = driver.find_element(By.ID, "user-message")
        message_field.send_keys("Hello World")

        show_message_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
        show_message_button.click()

        # user_message_field = driver.find_elements(By., 'Hello World')
        self.assertTrue("Hello World" in driver.page_source)


if __name__ == '__main__':
    unittest.main()
