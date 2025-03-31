from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestForConstructorSections:

    def test_for_buns_section(self, driver):
        driver.find_element(*Locators.SAUSES).click()
        driver.find_element(*Locators.BUNS).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUNS_TEXT))



    def test_for_sauses_section(self, driver):
        driver.find_element(*Locators.SAUSES).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SAUSES_TEXT))



    def test_for_fillings_section(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FILLINGS_TEXT))


