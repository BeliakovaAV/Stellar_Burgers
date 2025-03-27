from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import generate_registration_data
from locators import Locators
from curl import *


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
        assert driver.current_url == main_site + 'register'

        driver.quit()

    def test_registration_with_wrong_password(self, driver):
        # arrange
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.ACC_ENTRANCE).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys('12345')
        # act
        driver.find_element(*Locators.REG_BUTTON).click()
        error_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_POPUP)).text
        # assert
        assert error_text == 'Некорректный пароль'

        driver.quit()