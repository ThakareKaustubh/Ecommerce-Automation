import os

import allure
import yaml
from utils.config_loader import load_config
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--disable-gpu")  # Fixes issues in some systems
    chrome_options.add_argument("--window-size=1920x1080")  # Ensure elements are visible
    chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security (useful in Docker)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
    chrome_options.add_argument("--use-angle=default")
    chrome_options.add_argument("--start-maximized")  # Start maximized

    driver = webdriver.Chrome(chrome_options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs['driver_setup']
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )


@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]


@pytest.fixture(scope="session")
def test_data():
    # Load the data from the YAML file
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, '..', 'config', 'test_data.yaml')
    config_path = os.path.abspath(config_path)
    with open(config_path, "r") as file:
        return yaml.safe_load(file)