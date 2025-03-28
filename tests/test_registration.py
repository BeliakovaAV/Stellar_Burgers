from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import generate_registration_data
from locators import Locators
from curl import *
from data import *


class TestRegistrationWithNewCredentials:

    def test_successful_registration(self, driver):
        # arrange
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.ACC_ENTRANCE).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        # act
        driver.find_element(*Locators.REG_BUTTON).click()
        # assert
        assert driver.current_url == registration_page



    def test_registration_with_wrong_password(self, driver):
        # arrange
        driver.find_element(*Locators.ACC_ENTRANCE).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_NAME).send_keys(right_name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(wrong_password)
        # act
        driver.find_element(*Locators.REG_BUTTON).click()
        error_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_POPUP)).text
        # assert
        assert error_text == 'Некорректный пароль'

