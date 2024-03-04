from selenium import webdriver
import sys

sys.path.append('.')
from automationexercise_com.tests.conftest import register

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://automationexercise.com/')
    
    login_info = {"name" : 'tester T permanent jr.', 
                "email": 'permanent_user@test.com', 
                "password": 'StrongPassword!'}

    register(driver, login_info)
    
    driver.quit()
    
    
if __name__ == "__main__":
    main()