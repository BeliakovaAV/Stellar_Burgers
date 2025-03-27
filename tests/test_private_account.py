from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestPrivateAccount:

    def test_private_acc_button_entrance(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACC).click()
        assert WebDriverWait(driver, 5).until(EC.url_contains('account/profile'))

        driver.quit()

    def test_from_private_acc_to_constructor(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 5).until(EC.url_contains('account/profile'))
        driver.find_element(*Locators.CONSTRUCTOR).click()
        assert driver.current_url == main_site

        driver.quit()

    def test_from_private_acc_click_on_logo(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 5).until(EC.url_contains('account/profile'))
        driver.find_element(*Locators.SB_LOGO).click()
        assert driver.current_url == main_site

        driver.quit()

    def test_exit_from_private_acc(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 5).until(EC.url_contains('account/profile'))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.url_contains('login'))

        driver.quit()