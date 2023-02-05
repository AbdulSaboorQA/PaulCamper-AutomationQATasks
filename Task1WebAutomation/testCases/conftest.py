import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    base_url = ReadConfig.get_app_url()
    driver.get(base_url)
    yield driver
    driver.close()

    return driver

