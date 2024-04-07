from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3872988635&f_WT=2&geoId=100495523&keywords=" \
      "python%20developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER" \
      "&refresh=true"
LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")
PHONE_NUMBER = os.environ.get("MY_VERIFIED_NUMBER")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(URL)

WebDriverWait(driver, 5).until(
    ec.presence_of_element_located(
        (By.PARTIAL_LINK_TEXT, "Sign in"))
)

sign_in = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
sign_in.click()

# Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(LINKEDIN_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(LINKEDIN_PASSWORD)
password_field.send_keys(Keys.ENTER)

all_listings = driver.find_elements(By.CSS_SELECTOR(".job-card-container__link"))

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    save = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    save.click()
    time.sleep(1)

    follow = driver.find_element(By.CSS_SELECTOR, ".follow")
    follow.click()
    time.sleep(1)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button.click()
        time.sleep(5)

        phone_number = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone_number.text == "":
            phone_number.send_keys(PHONE_NUMBER)

        next_button = driver.find_element(By.CSS_SELECTOR, "artdeco-button")
        next_button.click()
        time.sleep(1)
        next_button.click()

        try:
            add_q_1 = driver.find_element(By.ID, "single-line-text-form-component-formElement-urn-li-jobs-applyformcommon"
                                                 "-easyApplyFormElement-3873225474-117576978-numeric")
            add_q_1.send_keys("3")

            add_q_2 = driver.find_element(By.ID, "single-line-text-form-component-formElement-urn-li-jobs-applyformcommon"
                                                 "-easyApplyFormElement-3873225474-117576970-numeric")
            add_q_2.send_keys("1")
            next_button.click()
            time.sleep(1)

            next_button.click()
        except NoSuchElementException:
            try:
                add_q_3 = driver.find_element(By.ID, "text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon"
                                                     "-easyApplyFormElement-3872988635-117831866-multipleChoice")
                # Create a Select object
                select = Select(add_q_3)
                # Select the option by value
                select.select_by_value("Professional")

                add_q_4 = driver.find_element(By.XPATH, "//label[@data-test-text-selectable-option__label='Yes']")
                add_q_4.click()

                add_q_5 = driver.find_element(By.ID, "text-entity-list-form-component-formElement-urn-li-jobs-"
                                                     "applyformcommon-easyApplyFormElement-3872077588-117700786-"
                                                     "multipleChoice")
                # Create a Select object
                select = Select(add_q_5)
                # Select the option by value
                select.select_by_value("Yes")

            except NoSuchElementException:
                next_button.click()

    except NoSuchElementException:
        print("No easy apply button, skipped.")
        continue
time.sleep(10)
driver.quit()
