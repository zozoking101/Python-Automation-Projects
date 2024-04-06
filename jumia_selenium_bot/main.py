from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.jumia.com.ng/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "fi-q"))
)

input_elem = driver.find_element(By.ID, "fi-q")
input_elem.clear()
input_elem.send_keys("instant pot" + Keys.ENTER)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//h3[@class='name'][contains(text(),'Instant Pot Multipurpose Instant Pot 13In1 "
                   "Duo Crisp 6.5L Ultimate Lid Multi-Cooker And Air Fryer')]"))
)

# Find the <h3> element with class "name" and target text content
link = driver.find_element(By.XPATH, "//h3[@class='name'][contains(text(),'Instant Pot Multipurpose Instant Pot 13In1 "
                                     "Duo Crisp 6.5L Ultimate Lid Multi-Cooker And Air Fryer')]")
driver.execute_script("arguments[0].click();", link)

# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located(
#         (By.XPATH, "//img[@data-src='https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/84"
#                    "/7806672/1.jpg?3224']"))
# )
#
# link = driver.find_element(By.XPATH, "//img[@data-src='https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)"
#                                      "/product/84/7806672/1.jpg?3224']")
# driver.execute_script("arguments[0].click();", link)

price = driver.find_element(By.CSS_SELECTOR, ".-i-ctr .-ubpt")
print(price.text)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[@type='button'][@class='add btn _prim -pea _i -fw']"))
)

button = driver.find_element(By.XPATH, "//button[@type='button'][@class='add btn _prim -pea _i -fw']")
button.click()

time.sleep(3)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//a[@class='-df -i-ctr -gy9 -hov-or5 -phs -fs16'][@href='/cart/']"))
)

cart = driver.find_element(By.XPATH, "//a[@class='-df -i-ctr -gy9 -hov-or5 -phs -fs16'][@href='/cart/']")
cart.click()

time.sleep(3)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//a[@class='btn _prim _md -fw'][@href='/checkout/summary/']"))
)

checkout = driver.find_element(By.XPATH, "//a[@class='btn _prim _md -fw'][@href='/checkout/summary/']")
checkout.click()

time.sleep(6)
driver.quit()
