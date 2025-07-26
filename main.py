rom  selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
from selenium.webdriver.common.keys import Keys
from  time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://www.linkedin.com/feed/")
email = "day32.pythonudemycourse@gmail.com"
password = "21070212"
number = 12345
username = driver.find_element(By.ID, value="username")
username.send_keys(email)
link_pass = driver.find_element(By.ID, value="password")
link_pass.send_keys(password)
link_pass.send_keys(Keys.ENTER)
sleep(5)
input("Press Enter after you have solved the captcha and are on the feed page...")
search = driver.find_element(By.CSS_SELECTOR, "input.search-global-typeahead__input")
search.send_keys("python developer")
search.send_keys(Keys.ENTER)
# Wait for the first job card to load and click it


# Wait for the Easy Apply button to appear and click it
easy_apply_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Easy apply')]"))
)
easy_apply_filter.click()
first_job = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "jobs-apply-button-id")))
first_job.click()

number_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-text-input--input")))
number_field.click()
number_field.send_keys(number)
number_field.send_keys(Keys.ENTER)
