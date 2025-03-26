import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Chrome(options=options)
    driver.get(main_site)

    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.ACC_EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.ACC_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.ENTER).click()

    return driver
