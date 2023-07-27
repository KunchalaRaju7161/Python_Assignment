from selenium import webdriver
from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

# open browser and maximize window
driver = webdriver.Chrome()
driver.maximize_window()
# wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
#                                                                        ElementNotVisibleException,
#                                                                        ElementNotSelectableException])
driver.implicitly_wait(5)
my_email = "rkunchala189@gmail.com"
my_password = "Raju@7161"

# Navigate to FB - url
driver.get("https://www.facebook.com/")

# verify the page is redirected to https://www.facebook.com/
current_url = driver.current_url
expected_url = "https://www.facebook.com/"

if current_url == expected_url:
    print("Page redirected successfully")
else:
    print(f"Page redirection faild. Expected : {expected_url},Actual : {current_url}")

# Verify that there is a "Create an account" section on the page
create_account = driver.find_element(By.XPATH, "//*[text()='Create new account']")
if create_account.is_displayed():
    print("Create an account section is present.")
else:
    print("Create an account section is not present.")

# click on create Account
create_account.click()

first_name = driver.find_element(By.NAME, "firstname")
first_name.send_keys('Raju')

sur_name = driver.find_element(By.NAME, "lastname")
sur_name.send_keys('Kunchala')

email_address = driver.find_element(By.NAME, "reg_email__")
email_address.send_keys('rkunchala189@gmail.com')

re_enter_email = driver.find_element(By.NAME, "reg_email_confirmation__")
re_enter_email.send_keys("rkunchala189@gmail.com")

password = driver.find_element(By.XPATH, "//input[@id='password_step_input']")
password.send_keys("Raju@7161")

day = Select(driver.find_element(By.XPATH, "//select[@id='day']"))
day.select_by_visible_text("15")

month = Select(driver.find_element(By.XPATH, "//select[@id='month']"))
month.select_by_visible_text("Aug")

year = Select(driver.find_element(By.XPATH, "//select[@id='year']"))
year.select_by_visible_text("1995")

gender = driver.find_element(By.XPATH, "//label[normalize-space()='Male']")
gender.click()

signUp_button = driver.find_element(By.XPATH, "//button[@name='websubmit']")
signUp_button.click()

time.sleep(10)

verification = driver.find_element(By.NAME, "code")
verification.send_keys("24874")
time.sleep(15)

confirm = driver.find_element(By.NAME, "confirm")
confirm.click()
time.sleep(10)
alert = driver.switch_to.alert
alert.accept()
time.sleep(20)


def is_logged_in(driver):
    try:
        profile_element = driver.find_element(By.XPATH, "//span[text()='Raju Kunchala']")
        print(profile_element.text)
        if profile_element.text() == "Raju Kunchala":
            return "login successfully"
        else:
            return "login failed"

    except:
        return False


is_logged_in(driver)

driver.quit()