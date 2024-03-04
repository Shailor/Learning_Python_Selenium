import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_contact_form(driver):
    assert 'Automation Exercise' in driver.title
    
    contact_buton = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a')
    if contact_buton.text == 'Contact us':
        contact_buton.click()
        
    assert 'Get In Touch' in driver.page_source
    
    # enter name
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[1]/input').send_keys('Test T jr.')
    # enter email
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[2]/input').send_keys('test@test.com')
    # enter subject
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[3]/input').send_keys('contact form test')
    # enter message
    driver.find_element(By.XPATH, '//*[@id="message"]').send_keys('Test message')
    # upload file
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[5]/input').send_keys(os.getcwd()+'/automationexercise_com/etc/Cat.jpg')
    # submit
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[6]/input').click()
    alert_present = False
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        alert_present = True
    except:
        alert_present = False
        
    assert alert_present
    assert 'Success! Your details have been submitted successfully.' in driver.page_source
    
    