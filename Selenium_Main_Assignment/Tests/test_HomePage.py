from Selenium_Main_Assignment.Configs.ConfigItems import ConfigItems
from Selenium_Main_Assignment.Pages.HomePage import HomePage
from Selenium_Main_Assignment.Tests.test_StartDriver import StartDriver
from Selenium_Main_Assignment.Utility.LogDetails import LogDetails
from Selenium_Main_Assignment.Utility.TakeScreenShot import TakeScreenShot


class Test_HomePage(StartDriver):
    logger = LogDetails.getLogger(ConfigItems.LOGGER_PATH)
    grocery_run_flag = False

    def test_home_page(self, driver):
        home_page = HomePage(driver)
        self.logger.info("Open this Store url :- https://www.demoblaze.com/")
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        ACTUAL_TITLE = home_page.get_header_text()
        self.logger.info("Check the Expected title is equal to Actual title")
        if ACTUAL_TITLE == ConfigItems.EXPECTED_HEADER:
            self.logger.info("Header validation passed.")
            print("Header validation passed.")
            TakeScreenShot.takeScreenShot(driver, "Header validation passed")

        else:
            self.logger.error(
                f"Header validation failed. Expected: '{ConfigItems.EXPECTED_HEADER}', Found: '{ACTUAL_TITLE}'")

            print(f"Header validation failed. Expected: '{ConfigItems.EXPECTED_HEADER}', Found: '{ACTUAL_TITLE}'")
            TakeScreenShot.takeScreenShot(self.driver, "Header validation failed")

    def test_footer(self,driver):
        home_page = HomePage(driver)
        self.logger.info("Open this Store url :- https://www.demoblaze.com/")
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        home_page.test_validate_footer_message()
        TakeScreenShot.takeScreenShot(driver, "Footer text")
