from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from vars import login_URL

chrome_driver_path = 'webdrivers/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("window-size=1200x600")

driver = webdriver.Chrome(
    service=ChromeService(executable_path=chrome_driver_path),
    options=chrome_options
    )