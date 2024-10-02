from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import constants


class TestRegistration:

    def test_registration_successful(self, driver):
        driver.get(constants.HOMEPAGE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(constants.REG_NAME)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(constants.REG_EMAIL)
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys(constants.REG_PASSWORD)
        driver.find_element(*Locators.REG_APPLY_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.LOGIN_PAGE_TITLE))
        assert driver.current_url == constants.LOGIN_URL

    def test_registration_with_invalid_password(self, driver):
        driver.get(constants.HOMEPAGE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(constants.REG_NAME)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(constants.REG_EMAIL)
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys(constants.REG_INVALID_PASSWORD)
        driver.find_element(*Locators.REG_APPLY_BUTTON).click()

        invalid_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.PASSWORD_ERROR))
        assert invalid_password.text == "Некорректный пароль"
