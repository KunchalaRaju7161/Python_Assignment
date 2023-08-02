import time

from selenium.webdriver.common.by import By

from Selenium_Main_Assignment.Pages.BasePage import BasePage
from Selenium_Main_Assignment.Tests.conftest import driver


class CartPage(BasePage):
    CART_ITEMS = (By.XPATH, "//a[contains(text(),'Delete')]/ancestor::tr[@class='success']//td[1]")
    DELETE_BUTTON = (By.XPATH, "//*[@id='tbodyid']/tr[1]/td[4]/a")

    PRODUCTS_NAME1 = (By.XPATH, "//tbody[@id='tbodyid']/tr[1]/td[2]")
    PRODUCTS_NAME2 = (By.XPATH, "//tbody[@id='tbodyid']/tr[2]/td[2]")

    PRODUCT_NAMES = (By.CSS_SELECTOR, ".product-name")
    PRODUCT_LINKS = (By.XPATH, "//a[@class='hrefch']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.maximize_window()

    def get_items_in_cart(self):
        global item_name
        list_of_Items = self.driver.find_elements(By.XPATH, self.CART_ITEMS)
        for i in list_of_Items:
            item_name = i.text
            print(item_name)
        return item_name


    def get_product_names(self):
        product_names = self.driver.find_elements(self.PRODUCT_NAMES)
        return [product_name.text for product_name in product_names]

    def delete_last_item_from_cart(self):
        self.do_click(self.DELETE_BUTTON)
        time.sleep(10)
        product_name1_text = self.get_element_text(self.PRODUCTS_NAME1)
        product_name2_text = self.get_element_text(self.PRODUCTS_NAME2)
        print(product_name2_text, product_name1_text)
        return product_name1_text, product_name2_text

