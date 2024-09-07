from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    tab_All_xpath = "//span[@class='hm-icon-label']"
    tab_SameDayDelivery_xpath = "//a[contains(text(),'Same-Day Delivery')]"
    tab_MedicalCare_xpath = "//span[normalize-space()='Medical Care']"
    tab_Prime_xpath = "//span[normalize-space()='Prime']"
    tab_AmazonBasics_xpath = "//a[normalize-space()='Amazon Basics']"
    tab_AmazonBusiness_xpath = "//span[normalize-space()='Amazon Business']"
    lnk_Careers_xpath = "//a[normalize-space()='Careers']"
    lnk_Sell_onAmazon_xpath = "//a[normalize-space()='Sell on Amazon']"
    lnk_Amazon_Visa_xpath = "//a[normalize-space()='Amazon Visa']"
    drp_Language_xpath = "//div[contains(@class,'icp-nav-globe-img-2 icp-button-globe-2')]"
    drp_Country_xpath = "//span[normalize-space()='United States']"
    button_AccountsLinks_xpath = "//span[normalize-space()='Account & Lists']"
    field_Search_xpath = "/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/input[1]"
    lnk_inside_drp_Account_xpath = "//span[normalize-space()='Account']"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def highlight_element(self, xpath):
        """ Highlights a WebElement by changing its CSS properties """
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        return element

    def disTabAll(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_All_xpath)))
        self.highlight_element(self.tab_All_xpath)

    def disTabSameDayDel(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_SameDayDelivery_xpath)))
        self.highlight_element(self.tab_SameDayDelivery_xpath)

    def disTabMedicalCar(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_MedicalCare_xpath)))
        self.highlight_element(self.tab_MedicalCare_xpath)

    def disTabPrime(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_Prime_xpath)))
        self.highlight_element(self.tab_Prime_xpath)

    def disAmazonBasics(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_AmazonBasics_xpath)))
        self.highlight_element(self.tab_AmazonBasics_xpath)

    def disCareers(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.lnk_Careers_xpath)))
        self.highlight_element(self.lnk_Careers_xpath)

    def disSell_onAmazon(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.lnk_Sell_onAmazon_xpath)))
        self.highlight_element(self.lnk_Sell_onAmazon_xpath)

    def disAmazon_Visa(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.lnk_Amazon_Visa_xpath)))
        self.highlight_element(self.lnk_Amazon_Visa_xpath)

    def disLanguage(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.drp_Language_xpath)))
        self.highlight_element(self.drp_Language_xpath)

    def disCountry(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.drp_Country_xpath)))
        self.highlight_element(self.drp_Country_xpath)


    def disSearch(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.field_Search_xpath)))
        self.highlight_element(self.field_Search_xpath)

    def disinside_drp_Account(self):
        account_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_AccountsLinks_xpath)))
        ActionChains(self.driver).move_to_element(account_link).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.lnk_inside_drp_Account_xpath)))
        self.highlight_element(self.lnk_inside_drp_Account_xpath)



