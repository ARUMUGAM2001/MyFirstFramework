import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from e2e_framework_building.page_object.checkout_confirmation import PurchasePage
from e2e_framework_building.page_object.login import LoginPage
from e2e_framework_building.page_object.shop import ShopPage

test_data_file="C:\\Users\\ARUMUGAM\\PycharmProjects\\PythonTestin\\e2e_framework_building\\test_data\\test_e2e_framework_building.json"
with open(test_data_file) as f:
    test_data = json.load(f)
    test_data_list=test_data["data"]

#passing test_data_list to test_list_item
@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_data_list)
def test_e2e(browser_instance,test_list_item):
    driver=browser_instance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    login_page = LoginPage(driver)
    print(login_page.get_title())
    login_page.login(test_list_item["user_name"],test_list_item["password"])
    shop_page = ShopPage(driver,test_list_item["product_name"])
    shop_page.add_product_to_cart()
    checkout=PurchasePage(driver)
    checkout.checkout()
    checkout.add_address("India")
    checkout.confirmation()
    time.sleep(3)