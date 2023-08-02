import time

from Selenium_Main_Assignment.Configs.ConfigItems import ConfigItems
from Selenium_Main_Assignment.Pages.HomePage import HomePage
from Selenium_Main_Assignment.Pages.Login_Page import Login_Page
from Selenium_Main_Assignment.Tests.test_StartDriver import StartDriver
from Selenium_Main_Assignment.Utility.LogDetails import LogDetails
from Selenium_Main_Assignment.Utility.TakeScreenShot import TakeScreenShot


class Test_Login_Page(StartDriver):
    logger = LogDetails.getLogger(ConfigItems.LOGGER_PATH)
    grocery_run_flag = False

    def test_signup_page(self, driver):
        home_page = HomePage(driver)
        self.logger.info("Open this Store url :- https://www.demoblaze.com/")
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        login_Page = Login_Page(driver)
        login_Page.login_user()
        time.sleep(5)
        TakeScreenShot.takeScreenShot(driver, "User Login ")