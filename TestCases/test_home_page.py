import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Home_Page:
    baseURL = ReadConfig.get_base_url()
    username = ReadConfig.getusername()
    password = ReadConfig.get_password()
    URL = ReadConfig.get_url()

    logger = LogGen.loggen()

    @pytest.mark.regression

    def test_els_Home_Page(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.homepage = HomePage(self.driver)
        self.homepage.disTabAll()
        self.homepage.disTabSameDayDel()
        self.homepage.disTabMedicalCar()
        self.homepage.disTabPrime()
        self.homepage.disAmazonBasics()
        self.homepage.disCareers()
        self.homepage.disSell_onAmazon()
        self.homepage.disAmazon_Visa()
        self.homepage.disLanguage()
        self.homepage.disCountry()
        self.homepage.disSearch()
        self.homepage.disinside_drp_Account()




