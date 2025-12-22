from selenium.webdriver.common.by import By

from e2e_framework_building.utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input=(By.ID, "username")
        self.password_input=(By.ID, "password")
        self.signin_button=(By.ID, "signInBtn")

    def login(self,user_name,password):
        self.driver.find_element(*self.username_input).send_keys(user_name)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()

