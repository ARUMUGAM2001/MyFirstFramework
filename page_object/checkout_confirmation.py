from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PurchasePage:
    def __init__(self,driver):
        self.driver = driver
        self.cart_validation=(By.CSS_SELECTOR, ".btn-success")
        self.search_country=(By.XPATH, "//input[@type='text']")
        self.country_found=(By.XPATH, "//a[text()='India']")
        self.select_country=(By.XPATH, "//label[@for='checkbox2']")
        self.purchase=(By.XPATH, "//input[@value='Purchase']")
        self.confirmation_message=(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def checkout(self):
        self.driver.find_element(*self.cart_validation).click()

    def add_address(self,country_name):
        self.driver.find_element(*self.search_country).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        #I require already an tuple so haven't mentioned *
        wait.until(expected_conditions.visibility_of_element_located(self.country_found)).click()
        self.driver.find_element(*self.select_country).click()
        self.driver.find_element(*self.purchase).click()

    def confirmation(self):
        message = self.driver.find_element(*self.confirmation_message).text
        print(message)