from driver import driver
from vars import login_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from vars import email, password
from utility import notify
from time import sleep

email_input_selector = '#UserId6'
password_input_selector = '#Password1'
login_btn_selector = '#btnSubmit'
verify_btn_selector = '#btnVerify'

if __name__ == "__main__":
    driver.get(login_URL)
    driver.find_element(By.CSS_SELECTOR, email_input_selector).send_keys(email)
    driver.find_element(By.CSS_SELECTOR, password_input_selector).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, verify_btn_selector).click()
    notify('Please solve captcha in 20 seconds')
    sleep(20)
    driver.find_element(By.CSS_SELECTOR, login_btn_selector).click()
    notify('Logged in successfully')
    sleep(20)


    

