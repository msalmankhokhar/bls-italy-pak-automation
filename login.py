from driver import driver
from vars import login_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from vars import email, password
from utility import notify
from time import sleep

email_input_selector = 'input[type="text"]'
password_input_selector = 'input[type="password"]'
login_btn_selector = '#btnSubmit'
verify_btn_selector = '#btnVerify'

if __name__ == "__main__":
    driver.get(login_URL)
    sleep(5)
    emailInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, email_input_selector)),
        message="Email input not found"
    )
    passwordInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, password_input_selector)),
        message="Password input not found"
    )
    verifyBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, verify_btn_selector)),
        message="Verify Button not found"
    )
    loginBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, login_btn_selector)),
        message="Login Btn not found"
    )
    driver.execute_script('arguments[0].setAttribute("value", arguments[1]);', emailInput, email)
    driver.execute_script('arguments[0].setAttribute("value", arguments[1]);', emailInput, password)
    verifyBtn.click()
    notify("Please solve captch in 10 seconds")