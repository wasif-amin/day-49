from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from  time import time, sleep
import random
ACCOUNT_EMAIL = "day32.pythonudemycourse@gmail.com"
ACCOUNT_PASSWORD = 21070212
PHONE_NUMBER = "7326745350"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()
    sleep(2)
    discard_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Discard']]")))
    discard_button.click()

def close_any_open_modals(current_driver, current_wait):


    try:
        discard_button = current_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Discard']]")), 3
        )
        discard_button.click()
        sleep(random.uniform(1, 2))
        main_dismiss_button = current_wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-modal__dismiss, .artdeco-modal__dismiss button")),
            3
        )
        main_dismiss_button.click()
    except TimeoutException:
        print("  No active modal or confirmation dialog found to close, or they closed automatically.")
    except NoSuchElementException:
        print("  No modal elements found to close.")





driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Click Reject Cookies Button
sign_in =driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in.click()
EMAIL_INPUT = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
EMAIL_INPUT.click()
EMAIL_INPUT.send_keys(ACCOUNT_EMAIL)
PASSWORD_INPUT = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
PASSWORD_INPUT.click()
PASSWORD_INPUT.send_keys(ACCOUNT_PASSWORD)
SIGN_IN_INPUT = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
SIGN_IN_INPUT.click()
sleep(3)
# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
jobs = []
for job in all_listings:
    if  "Easy Apply" in job.text:
        jobs.append(job)
# Apply for Jobs
for listing in jobs:
    close_any_open_modals(driver, wait)
    print("Opening Listing")
    listing.click()
    sleep(2)


    try:
        # Click Apply Button
        apply_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-s-apply button")),
            5
        )
        apply_button.click()
        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        phone.clear()
        phone.send_keys(PHONE_NUMBER)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

sleep(5)
driver.quit()
