from Selenium_Main_Assignment.Pages.CartPage import CartPage
from Selenium_Main_Assignment.Utility.LogDetails import LogDetails
from Selenium_Main_Assignment.Configs.ConfigItems import ConfigItems
from Selenium_Main_Assignment.Pages.HomePage import HomePage
from Selenium_Main_Assignment.Tests.test_StartDriver import StartDriver


class Test_CartPage(StartDriver):
    logger = LogDetails.getLogger(ConfigItems.LOGGER_PATH)

    def test_delete_to_cart(self, driver):
        home_page = HomePage(driver)
        cart_page = CartPage(driver)
        self.logger.info("Open this Store url :- https://www.demoblaze.com/cart.html#")
        home_page.open(ConfigItems.CART_URL)

        Items = cart_page.get_cart_items_count()
        print(Items)

    def test_print_items(self, driver):
        cart_page = CartPage(driver)
        cart_page.delete_last_item_from_cart()
