from Tests.conftest import driver
from Tests.test_StartDriver import StartDriver
from Pages.PlaceOrderPage import OrderPage
from Pages.HomePage import HomePage
from Configs.ConfigItems import ConfigItems
from Utility.LogDetails import LogDetails


class Test_OrderPage(StartDriver):
    logger = LogDetails.getLogger(ConfigItems.LOGGER_PATH)
    grocery_run_flag = False

    def test_phone_select_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        self.logger.info("Open this Store url :- https://www.demoblaze.com/")
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        phone_text, phone_cart_text = order_page.order_phone_cart()
        print(phone_text, phone_cart_text)
        assert phone_text == phone_cart_text

    def test_laptop_select_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        self.logger.info("Open this Store url :- https://www.demoblaze.com/")
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        laptop_text, laptop_cart_text = order_page.order_laptop_cart()
        print(laptop_text, laptop_cart_text)
        assert laptop_text == laptop_cart_text

    def test_monitor_select_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        self.logger.info("Open this Store url :- https://www.demoblaze.com/")
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        monitor_text, monitor_cart_text = order_page.order_monitors_cart()
        print(monitor_text, monitor_cart_text)
        assert monitor_text == monitor_cart_text
