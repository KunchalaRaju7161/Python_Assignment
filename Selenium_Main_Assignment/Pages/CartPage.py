from selenium.webdriver.common.by import By

from Configs.ConfigItems import ConfigItems
from Pages.BasePage import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.XPATH, "//tr[@class='success']")
    DELETE_BUTTON = (By.XPATH, "//a[contains(text(),'Delete')]")

    PRODUCT_LINKS = (By.XPATH, "//a[@class='hrefch']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.maximize_window()

    def get_cart_items_count(self):
        return len(self.driver.find_elements(self.CART_ITEMS))

    def delete_last_item_from_cart(self):
        cart_items = self.driver.find_elements(self.CART_ITEMS)
        cart_items[-1].find_element(self.DELETE_BUTTON).click()
