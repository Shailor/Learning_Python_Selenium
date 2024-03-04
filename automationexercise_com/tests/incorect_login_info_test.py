import pytest

from conftest import login

def test_login_wiht_incorrect_info(driver, login_info):
    incorrect_login_data = {'email': 'wrong@email.com', "password": "wrong_password"}
    
    login(driver, incorrect_login_data)
    
    assert 'Your email or password is incorrect!' in driver.page_source
    