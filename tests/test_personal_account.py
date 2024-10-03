from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators


class TestPersonalAccount:

    def test_navigate_to_personal_account(self, driver, authorization):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(constants.PERSONAL_ACCOUNT_URL)
        )
        assert driver.current_url == constants.PERSONAL_ACCOUNT_URL

    def test_navigate_from_personal_account_to_constructor(self, driver, authorization):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(constants.PERSONAL_ACCOUNT_URL)
        )
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.current_url == constants.HOMEPAGE_URL

    def test_navigate_from_personal_account_to_logo(self, driver, authorization):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(constants.PERSONAL_ACCOUNT_URL)
        )
        driver.find_element(*Locators.LOGO).click()
        assert driver.current_url == constants.HOMEPAGE_URL

    def test_logout_from_personal_account(self, driver, authorization):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(constants.PERSONAL_ACCOUNT_URL)
        )
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(constants.LOGIN_URL)
        )
        assert driver.current_url == constants.LOGIN_URL
