from data import Credentials
from locators import Locators
from curl import *


class TestWaysToEnterTheService:

    def test_via_acc_entrance_button_on_main(self, driver):
        driver.find_element(*Locators.ACC_ENTRANCE).click()
        driver.find_element(*Locators.ACC_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ACC_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER).click()
        assert driver.current_url == main_site + 'login'

        driver.quit()

    def test_via_private_acc_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACC).click()
        driver.find_element(*Locators.ACC_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ACC_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER).click()
        assert driver.current_url == main_site + 'login'

        driver.quit()

    def test_via_reg_page(self, driver):
        driver.find_element(*Locators.ACC_ENTRANCE).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.ENTER_REG_PAGE).click()
        driver.find_element(*Locators.ACC_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ACC_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER).click()
        assert driver.current_url == main_site + 'login'

        driver.quit()

    def test_via_password_reset_page_button(self, driver):
        driver.find_element(*Locators.ACC_ENTRANCE).click()
        driver.find_element(*Locators.RESET_PASS_LINK).click()
        driver.find_element(*Locators.FORGOT_PASS_LINK).click()
        driver.find_element(*Locators.ACC_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ACC_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER).click()
        assert driver.current_url == main_site + 'login'

        driver.quit()
