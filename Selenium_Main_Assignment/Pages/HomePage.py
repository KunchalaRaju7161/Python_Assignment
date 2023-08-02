# import necessary modules
from selenium.webdriver.common.by import By
from selenium import webdriver
from Selenium_Main_Assignment.Pages.BasePage import BasePage
from Selenium_Main_Assignment.Configs.ConfigItems import ConfigItems


class HomePage(BasePage):
    HEADER_TEXT = "//a[@id='nava']/text()"

    CART_BUTTON = (By.ID, "cartur")
    FOOTER =(By.XPATH, "//p[contains(text(),'Copyright © Product Store 2017')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.get(ConfigItems.PRODUCT_STORE_URL)

    def open(self, url):
        self.driver.get(url)

    def get_header_text(self):
        title = self.driver.title
        return title

    def test_validate_footer_message(self):
        footer_element = self.get_element_text(self.FOOTER)
        print(footer_element)
        assert footer_element == ConfigItems.EXPECTED_FOOTER
