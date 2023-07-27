from selenium import webdriver
from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

driver.maximize_window()
wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                       ElementNotVisibleException,
                                                                       ElementNotSelectableException])
driver.get("https://www.gmail.com")


my_email = "rkunchala189@gmail.com"
my_password = "Raju@7161"
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
email_input.send_keys(my_email)

email_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
email_next_button.click()
time.sleep(10)

password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
password_input.send_keys(my_password)

password_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
password_next_button.click()

primary_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Primary']")))
is_primary_select = primary_tab.get_attribute("aria-selected")

if not is_primary_select:
    primary_tab.click()
time.sleep(15)

index_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-tooltip='Inbox']")))
email_count = int(index_tab.text)
print("Total email in Primary tab is : ", email_count)


def get_email_info(email_index):
    email_xpath = f"//div[@data-role='primaryTab']//div[@role='main']//tr[{email_index}]"
    sender = driver.find_element(By.XPATH, f"{email_xpath}/td[@data-act='from']/span/span").text
    subject = driver.find_element(By.XPATH, f"{email_xpath}/td[@data-act='subject']/span/span").text
    return sender, subject


# Replace `N` with the index of the email you want to retrieve (1-indexed)
N = 1  # Example: Get info for the first email
sender, subject = get_email_info(N)
print(f"Sender of email {N}: {sender}")
print(f"Subject of email {N}: {subject}")

driver.quit()
