import openpyxl
import pytest

from Selenium_Main_Assignment.Pages.CartPage import CartPage
from Selenium_Main_Assignment.Utility.LogDetails import LogDetails
from Selenium_Main_Assignment.Configs.ConfigItems import ConfigItems
from Selenium_Main_Assignment.Pages.HomePage import HomePage
from Selenium_Main_Assignment.Pages.PlaceOrderPage import OrderPage
from Selenium_Main_Assignment.Pages.RegisterPage import RegisterPage
from Selenium_Main_Assignment.Tests.test_StartDriver import StartDriver
from Selenium_Main_Assignment.Utility.TakeScreenShot import TakeScreenShot


class Test_OrderPage(StartDriver):
    logger = LogDetails.getLogger(ConfigItems.LOGGER_PATH)
    grocery_run_flag = False
    takeScreenShot = TakeScreenShot()

    def test_phone_select_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        self.logger.info("Open this Store url :- https://www.demoblaze.com/")
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        phone_text, phone_cart_text = order_page.order_phone_cart()
        print(phone_text, phone_cart_text)
        self.logger.info(f"Phone selected: {phone_text}, Phone in cart: {phone_cart_text}")
        assert phone_text == phone_cart_text
        # TakeScreenShot.takeScreenShot(self.driver, "Validate Phone text")

    def test_laptop_select_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        screen_shot = TakeScreenShot()
        self.logger.info("Open this Store url :- https://www.demoblaze.com/")
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        self.laptop_text, laptop_cart_text = order_page.order_laptop_cart()
        print(self.laptop_text, laptop_cart_text)
        self.logger.info(f"Laptop selected: {self.laptop_text}, Laptop in cart: {laptop_cart_text}")
        assert self.laptop_text == laptop_cart_text
        # screen_shot.takeScreenShot(self.driver, "Validate Laptop text")

    def test_monitor_select_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        self.logger.info("Open this Store url :- https://www.demoblaze.com/")
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        self.monitor_text, monitor_cart_text = order_page.order_monitors_cart()
        print(self.monitor_text, monitor_cart_text)
        self.logger.info(f"Monitor selected: {self.monitor_text}, Monitor in cart: {monitor_cart_text}")
        assert self.monitor_text == monitor_cart_text

    def test_delete_product_cart(self, driver):
        cart_page = CartPage(driver)

        self.product_name1, self.product_name2 = cart_page.delete_last_item_from_cart()

    def test_order_place(self, driver):
        register_page = RegisterPage(driver)
        thank_you_message_text, purchase_detail_text = register_page.register_user()
        print(thank_you_message_text, purchase_detail_text)
        self.logger.info(f"Thank You Message: {thank_you_message_text}, Purchase Details: {purchase_detail_text}")
        assert thank_you_message_text == "Thank you for your purchase!"

    def test_return_to_homepage(self, driver):
        home_page = HomePage(driver)
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        ACTUAL_TITLE = home_page.get_header_text()
        if ACTUAL_TITLE == ConfigItems.EXPECTED_HEADER:
            print("Homepage return validation passed.")
            self.logger.info("Homepage return validation passed.")
