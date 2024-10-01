from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestPersonalAccount:

    def test_navigate_to_personal_account(self, driver, authorization):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_navigate_from_personal_account_to_constructor(self, driver, authorization):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
        )
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_navigate_from_personal_account_to_logo(self, driver, authorization):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
        )
        driver.find_element(*Locators.LOGO).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_logout_from_personal_account(self, driver, authorization):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
        )
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
