import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser name"
    )

@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":


        options = webdriver.ChromeOptions()
        prefs = {
            # stop “save password” popups
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,

            # stop “password leaked/weak” warning / safety check UI
            "profile.password_manager_leak_detection": False,
        }
        options.add_experimental_option("prefs", prefs)

        # optional: reduces other chrome UI interruptions
        options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    else:
        raise ValueError("Unsupported browser")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()