from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_phone_email_id = "ap_email"
    button_continue_xpath = "//input[@id='continue']"
    textbox_password_id = "ap_password"
    button_login_xpath = "//input[@id='signInSubmit']"
    title_id = "Your Amazon.com"
    link_logout_link_text = "Logout"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def setUserName(self, username):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_phone_email_id))).clear()
        self.driver.find_element(By.ID, self.textbox_phone_email_id).send_keys(username)

    def clickContinue(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_continue_xpath))).click()

    def setPassword(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_password_id))).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))).click()

    def clickLogout(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.link_logout_link_text))).click()
