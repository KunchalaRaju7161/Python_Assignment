from Configs.ConfigItems import ConfigItems
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Tests.test_StartDriver import StartDriver
from Utility.LogDetails import LogDetails
from Pages.CartPage import CartPage


class Test_CartPage(StartDriver):
    logger = LogDetails.getLogger(ConfigItems.LOGGER_PATH)

    # def test_delete_to_cart(self, driver):
    #     home_page = HomePage(driver)
    #     cart_page = CartPage(driver)
    #     self.logger.info("Open this Store url :- https://www.demoblaze.com/")
    #     home_page.open(ConfigItems.CART_URL)
    #
    #     Items = cart_page.get_cart_items_count()
    #     print(Items)
