import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_sorting(browser_instance):
    driver=browser_instance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    elements = driver.find_elements(By.XPATH, "//tr/td[1]")
    original_element = []
    for element in elements:
        original_element.append(element.text)
    copy_original_element = original_element.copy()
    copy_original_element.sort()
    assert original_element == copy_original_element, f"Original element: {original_element} does not matches copy: {copy_original_element}"
    print(f"Original element: {original_element}matches copy: {copy_original_element}")
    time.sleep(2)