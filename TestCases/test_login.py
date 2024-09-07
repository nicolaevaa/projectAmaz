import pytest
import time
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test001Login:
    baseURL = ReadConfig.get_base_url()
    username = ReadConfig.getusername()
    password = ReadConfig.get_password()
    URL = ReadConfig.get_url()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(10)
        print(f"Actual Title: {act_title}")  # Print the title to the console for debugging

        # Check if the actual title matches the expected title
        if act_title == "Amazon.com":
            assert True
            self.logger.info("********************Test is Passed!*******************")
        else:
            # If the title doesn't match, save a screenshot and log failure
            self.driver.save_screenshot("./Screenshots/" + "test_home_pageTitle.png")
            self.logger.info(
                f"********************Test is Failed! Expected Title: 'Amazon Sign-In' but got '{act_title}' *******************")
            self.driver.close()  # Close the driver
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.close()

    @pytest.mark.sanity
    def test_home_pageTitle2(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your Amazon.com":
            assert True
            self.logger.info("********************Test is Passed!*******************")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_home_pageTitle2.png")
            self.driver.close()
            self.logger.info("********************Test is Failed!*******************")
            assert False
