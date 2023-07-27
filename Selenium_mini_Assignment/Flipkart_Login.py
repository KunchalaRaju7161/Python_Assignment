from selenium import webdriver
from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://www.flipkart.com")
time.sleep(10)
# email_input = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
# email_input.send_keys("rkunchala189@gmail.com")
phone_input = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
phone_input.send_keys("7090846422")
time.sleep(3)
request_OTP = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
request_OTP.click()
time.sleep(15)

# profile_element = driver.find_element(By.XPATH, "//div[@class='exehdJ'][1]")
profile_element = driver.find_element(By.XPATH, "//div[text()='Raju']")

print(profile_element.text)
time.sleep(20)


def is_logged_in(profile_element):
    try:

        if profile_element.text() == "Raju":
            return "login successfully"
        else:
            return "login failed"

    except:
        return False


time.sleep(15)
is_logged_in(profile_element)

time.sleep(10)
driver.close()
