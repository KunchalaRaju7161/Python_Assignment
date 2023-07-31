from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# create BasePage class
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Custom wait for element visibility before interaction with it
    def do_wait(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # Get a list of web elements that match the given Xpath
    def get_list(self, xpath_string):
        by_locator = (By.XPATH, xpath_string)
        self.do_wait(by_locator)
        list_of_webelements = self.driver.find_elements(By.XPATH, xpath_string)
        return list_of_webelements

    # Move the mouse cursor to the given element
    def move_cursor(self, by_locator):
        actions = ActionChains(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        actions.move_to_element(self.driver.find_element(by_locator)).perform()

    # Move the mouse cursor to the required element identified by the given Xpath
    def move_cursor_to_required_element(self, xpath_string):
        by_locator = (By.XPATH, xpath_string)
        actions = ActionChains(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        actions.move_to_element(self.driver.find_element(By.XPATH, xpath_string)).perform()

    # Custom wait for elements visibility before sending input text to it
    def do_send_keys(self, by_locator, input_text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(input_text)

    # Get the visible text of the elements identified by the given locator
    def get_text(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    # Check if an elements identified by the given locators is enabled and visible
    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # Get the page title and wait until it matches the provided title
    def get_page_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title


