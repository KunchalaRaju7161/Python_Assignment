# import necessary modules
from selenium.webdriver.common.by import By
from selenium import webdriver
from Configs.ConfigItems import ConfigItems
from Pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER_TEXT = "//a[@id='nava']/text()"

    CART_BUTTON = (By.ID, "cartur")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.get(ConfigItems.PRODUCT_STORE_URL)

    def open(self, url):
        self.driver.get(url)

    def get_header_text(self):
        title = self.driver.title
        return title
