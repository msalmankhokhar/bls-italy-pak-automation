from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from vars import login_URL

chrome_driver_path = 'webdrivers/chromedriver.exe'

driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path))