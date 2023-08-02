from Selenium_Main_Assignment.Configs.ConfigItems import ConfigItems
from Selenium_Main_Assignment.Pages.HomePage import HomePage
from Selenium_Main_Assignment.Pages.SignUp_Page import SignUp_Page
from Selenium_Main_Assignment.Tests.test_StartDriver import StartDriver
from Selenium_Main_Assignment.Utility.LogDetails import LogDetails


class Test_SignUp_Page(StartDriver):
    def test_signup_page(self, driver):
        home_page = HomePage(driver)
        home_page.open(ConfigItems.PRODUCT_STORE_URL)
        signUp_Page = SignUp_Page(driver)
        signUp_Page.sign_up_user()




