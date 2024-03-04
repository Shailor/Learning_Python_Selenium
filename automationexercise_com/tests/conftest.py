import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


chrome_options = Options()
chrome_options.add_experimental_option("detach",True)




@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get('https://automationexercise.com/')
    yield driver
    driver.quit()
    

@pytest.fixture
def login_info():
    login_info = {
        'name':  'tester T jr.',
        'email': 'asdf@test.com' , 
        'password': 'StrongPassword!'
        }
    return login_info

@pytest.fixture
def login_info_permanent_user():
        login_info = {
            "name" : 'tester T permanent jr.', 
            "email": 'permanent_user@test.com', 
            "password": 'StrongPassword!'
            }
        return login_info
    
    
def register(driver, login_info):
    # Get to login page
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
    
    assert driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/h2').text == 'New User Signup!'
    
    # Enter name
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys(login_info.get('name'))
    # Enter email
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys(login_info.get('email'))
    # click on signup button
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()
    
    # Verify that registration form is open
    assert "Enter Account Information" in driver.page_source
    
    # select Title
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/form/div[1]/div[1]/label').click()
    # enter password
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(login_info.get('password'))
    # enter Date of birth
    Select(driver.find_element(By.XPATH, '//*[@id="days"]')).select_by_visible_text("1")
    Select(driver.find_element(By.XPATH, '//*[@id="months"]')).select_by_visible_text("January")
    Select(driver.find_element(By.XPATH, '//*[@id="years"]')).select_by_visible_text("2000")
    
    # subscribe to newsletter and partner offers
    driver.find_element(By.XPATH, '//*[@id="newsletter"]').click()
    driver.find_element(By.XPATH, '//*[@id="optin"]').click()
    
    # enter First Name
    driver.find_element(By.XPATH, '//*[@id="first_name"]').send_keys("Test")
    # enter Last Name
    driver.find_element(By.XPATH, '//*[@id="last_name"]').send_keys("Test")
    # enter Company
    driver.find_element(By.XPATH, '//*[@id="company"]').send_keys("Test Inc.")
    # enter Address
    driver.find_element(By.XPATH, '//*[@id="address1"]').send_keys("123 Test street")
    driver.find_element(By.XPATH, '//*[@id="address2"]').send_keys("Apartment 456")
    # select Country
    Select(driver.find_element(By.XPATH, '//*[@id="country"]')).select_by_visible_text("United States")
    # enter State
    driver.find_element(By.XPATH, '//*[@id="state"]').send_keys("NY")
    # enter City
    driver.find_element(By.XPATH, '//*[@id="city"]').send_keys('NY')
    # enter Zip Code
    driver.find_element(By.XPATH, '//*[@id="zipcode"]').send_keys("123")
    # enter Mobile Number
    driver.find_element(By.XPATH, '//*[@id="mobile_number"]').send_keys('456')
    
    # create account
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/form/button').click()



def login(driver, login_info):

    
    # get to login page
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
    assert driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/h2').text == 'New User Signup!'
    
    # enter email
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys(login_info.get('email'))
    # enter password
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys(login_info.get('password'))
    # click Login
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()
    
    
def delete_user(driver):
    delete_button = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    if delete_button.text == "Delete Account":
        delete_button.click()
    else:
        return False


def close_ads(driver):
    time.sleep(1)
    driver.execute_script("""
    const elements = document.getElementsByClassName("google-auto-placed");
    while (elements.length > 0) elements[0].remove();
                        """)

    time.sleep(1)
    driver.execute_script("""
    const elements = document.getElementsByClassName("adsbygoogle adsbygoogle-noablate");
    while (elements.length > 0) elements[0].remove();
                        """)