from selenium import webdriver
from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                       ElementNotVisibleException,
                                                                       ElementNotSelectableException])

driver.get("http://www.flipkart.com")
driver.refresh()
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='_2IX_2- VJZDxU']")))
# email_input = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
# email_input.send_keys("rkunchala189@gmail.com")
phone_input = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
phone_input.send_keys("7090846422")

element1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")))
request_OTP = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
request_OTP.click()
time.sleep(20)


def is_logged_in(driver):
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'exehdJ')]")))
        profile_element = driver.find_element(By.XPATH, "//div[contains(@class, 'exehdJ')]")
        print(profile_element.text)
        if profile_element.text() == "Raju":
            return "login successfully"
        else:
            return "login failed"

    except:
        return False


is_logged_in(driver)

time.sleep(10)
driver.close()
