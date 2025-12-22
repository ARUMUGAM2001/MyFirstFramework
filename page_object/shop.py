from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self,driver,product_name):
        self.driver = driver
        self.product_name = product_name
        self.shop_page=(By.LINK_TEXT, "Shop")
        self.select_product=(By.XPATH,"//app-card/div/div/h4/a[text()='" + product_name + "']/parent::h4/parent::div/parent::div/div[@class='card-footer']/button")
        self.check_out=(By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def add_product_to_cart(self):
        self.driver.find_element(*self.shop_page).click()
        self.driver.find_element(*self.select_product).click()
        self.driver.find_element(*self.check_out).click()
