from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import constants


class TestLogin:

    def test_login_with_account_login_button(self, driver, homepage):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.LOGIN_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.LOGIN_PASSWORD)
        driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(constants.HOMEPAGE_URL))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_enabled()

    def test_login_with_personal_account_button(self, driver, homepage):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.LOGIN_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.LOGIN_PASSWORD)
        driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(constants.HOMEPAGE_URL))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_enabled()

    def test_login_with_login_button_on_registration_page(self, driver, homepage):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.REG_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.LOGIN_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.LOGIN_PASSWORD)
        driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(constants.HOMEPAGE_URL))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_enabled()

    def test_login_with_login_button_on_reset_pw_page(self, driver, homepage):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.RESET_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.RES_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.LOGIN_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.LOGIN_PASSWORD)
        driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(constants.HOMEPAGE_URL))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_enabled()
