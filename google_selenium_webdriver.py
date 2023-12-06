from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# chrome_driver_path = 'C:\Users\donke\Downloads\Compressed\chrome-win64\chrome-win64\chrome.exe'

# new_driver = webdriver.Chrome(chrome_driver_path)
# new_driver.get('https://www.appmillers.com')

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')

time.sleep(100)

driver.quit()