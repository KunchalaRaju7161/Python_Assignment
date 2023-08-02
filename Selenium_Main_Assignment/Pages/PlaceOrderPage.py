import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from Selenium_Main_Assignment.Pages.BasePage import BasePage


class OrderPage(BasePage):
    LAPTOP_CATEGORY = (By.XPATH, "//a[contains(text(),'Laptops')]")
    PHONE_CATEGORY = (By.XPATH, "//a[contains(text(),'Phones')]")
    MONITOR_CATEGORY = (By.XPATH, "//a[contains(text(),'Monitors')]")

    PHONE_SELECT = (By.XPATH, "//div[@id='tbodyid']/div[2]/div/div/h4[@class='card-title']")
    MONITOR_SELECT = (By.XPATH, "//div[@id='tbodyid']/div[2]/div/div/h4[@class='card-title']")
    LAPTOP_SELECT = (By.XPATH, "//div[@id='tbodyid']/div[2]/div/div/h4[@class='card-title']")

    ADD_CART = (By.XPATH, "//a[contains(text(),'Add to cart')]")
    PHONE_NAME_TEXT = (By.XPATH, "//h2[@class='name']")
    CART_TAB = (By.XPATH, "//a[contains(text(),'Cart')]")
    PHONE_CART_TEXT = (By.XPATH, "//td[text()='820']/ancestor::tr[@class='success']//td[text()='Nokia lumia 1520']")

    LAPTOP_NAME_TEXT = (By.XPATH, "//h2[@class='name']")
    LAPTOP_CART_TEXT = (
    By.XPATH, "//td[contains(text(),'790')]/ancestor::tr[@class='success']//td[contains(text(),'Sony vaio i7')]")

    MONITOR_NAME_TEXT = (By.XPATH, "//h2[@class='name']")
    MONITOR_CART_TEXT = (
    By.XPATH, "//td[contains(text(),'230')]/ancestor::tr[@class='success']//td[contains(text(),'ASUS Full HD')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.maximize_window()

    def order_phone_cart(self):
        self.wait_for_element(locator=self.PHONE_CATEGORY)
        self.element = self.get_element(locator=self.PHONE_CATEGORY, locator_type="xpath")
        # self.element.click()
        self.do_click(self.PHONE_CATEGORY)

        self.wait_for_element(locator=self.PHONE_SELECT)
        element = self.get_element(locator=self.PHONE_SELECT, locator_type="xpath")
        self.do_click(self.PHONE_SELECT)

        self.wait_for_element(locator=self.PHONE_NAME_TEXT)
        element = self.get_element(locator=self.PHONE_NAME_TEXT, locator_type="xpath")
        phone_text = self.get_element_text(self.PHONE_NAME_TEXT)

        self.wait_for_element(locator=self.ADD_CART)
        element = self.get_element(locator=self.ADD_CART, locator_type="xpath")
        self.do_click(self.ADD_CART)
        time.sleep(5)
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()

        self.wait_for_element(locator=self.CART_TAB)
        element = self.get_element(locator=self.CART_TAB, locator_type="xpath")
        self.do_click(self.CART_TAB)

        self.wait_for_element(locator=self.PHONE_CART_TEXT)
        element = self.get_element(locator=self.PHONE_CART_TEXT, locator_type="xpath")

        phone_cart_text = self.get_element_text(self.PHONE_CART_TEXT)
        return phone_text, phone_cart_text

    def order_laptop_cart(self):
        self.wait_for_element(locator=self.LAPTOP_CATEGORY)
        self.element = self.get_element(locator=self.LAPTOP_CATEGORY, locator_type="xpath")
        # self.element.click()
        self.do_click(self.LAPTOP_CATEGORY)

        self.wait_for_element(locator=self.LAPTOP_SELECT)
        element = self.get_element(locator=self.LAPTOP_SELECT, locator_type="xpath")
        self.do_click(self.LAPTOP_SELECT)

        self.wait_for_element(locator=self.LAPTOP_NAME_TEXT)
        element = self.get_element(locator=self.LAPTOP_NAME_TEXT, locator_type="xpath")

        # laptop_text = self.get_element_text(self.LAPTOP_NAME_TEXT)
        laptop_text = self.get_element_text(self.LAPTOP_NAME_TEXT)

        self.wait_for_element(locator=self.ADD_CART)
        element = self.get_element(locator=self.ADD_CART, locator_type="xpath")
        self.do_click(self.ADD_CART)
        time.sleep(5)
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()

        self.wait_for_element(locator=self.CART_TAB)
        element = self.get_element(locator=self.CART_TAB, locator_type="xpath")
        self.do_click(self.CART_TAB)

        self.wait_for_element(locator=self.LAPTOP_CART_TEXT)
        element = self.get_element(locator=self.LAPTOP_CART_TEXT, locator_type="xpath")
        laptop_cart_text = self.get_element_text(self.LAPTOP_CART_TEXT)

        return laptop_text, laptop_cart_text

    def order_monitors_cart(self):
        self.wait_for_element(locator=self.MONITOR_CATEGORY)
        self.element = self.get_element(locator=self.MONITOR_CATEGORY, locator_type="xpath")
        # self.element.click()
        self.do_click(self.MONITOR_CATEGORY)

        self.wait_for_element(locator=self.MONITOR_SELECT)
        element = self.get_element(locator=self.MONITOR_SELECT, locator_type="xpath")
        self.do_click(self.MONITOR_SELECT)

        self.wait_for_element(locator=self.MONITOR_NAME_TEXT)
        element = self.get_element(locator=self.MONITOR_NAME_TEXT, locator_type="xpath")

        # laptop_text = self.get_element_text(self.LAPTOP_NAME_TEXT)
        monitor_text = self.get_element_text(self.MONITOR_NAME_TEXT)

        self.wait_for_element(locator=self.ADD_CART)
        element = self.get_element(locator=self.ADD_CART, locator_type="xpath")
        self.do_click(self.ADD_CART)
        time.sleep(5)
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()

        self.wait_for_element(locator=self.CART_TAB)
        element = self.get_element(locator=self.CART_TAB, locator_type="xpath")
        self.do_click(self.CART_TAB)

        self.wait_for_element(locator=self.MONITOR_CART_TEXT)
        element = self.get_element(locator=self.MONITOR_CART_TEXT, locator_type="xpath")
        monitor_cart_text = self.get_element_text(self.MONITOR_CART_TEXT)

        return monitor_text, monitor_cart_text

