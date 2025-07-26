from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from  time import sleep
email = "day32.pythonudemycourse@gmail.com"
password = "21070212"
number = 7326745350

# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)
sign_in =driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in.click()
EMAIL_INPUT = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
EMAIL_INPUT.click()
EMAIL_INPUT.send_keys(email)
PASSWORD_INPUT = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
PASSWORD_INPUT.click()
PASSWORD_INPUT.send_keys(password)
SIGN_IN_INPUT = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
SIGN_IN_INPUT.click()
sleep(3)
easy_apply_button = WebDriverWait(driver, 10).until( # Added (driver, 10)
     EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Easy Apply']]"))
 )
easy_apply_button.click()

num_field = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, '//input[contains(@id, "phoneNumber-nationalNumber")]'))
 )
num_field.click()
num_field.send_keys(number)

next_1 = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Next']]"))
 )
next_1.click()

review = WebDriverWait(driver, 30).until(
  EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Review']]"))
 )
review.click()
# #
submit_application_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Submit application']]")))
submit_application_button.click()
