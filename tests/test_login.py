from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By


class TestLogin:

    def test_login_with_account_login_button(self, driver, homepage):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('chizhevskiy_kirill_14_123@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123123')
        driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Оформить заказ")]')))
        assert driver.find_element(By.XPATH, '//button[contains(text(), "Оформить заказ")]').is_enabled()

    def test_login_with_personal_account_button(self, driver, homepage):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('chizhevskiy_kirill_14_123@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123123')
        driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.find_element(By.XPATH, '//button[contains(text(), "Оформить заказ")]').is_enabled()

    def test_login_with_login_button_on_registration_page(self, driver, homepage):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.REG_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('chizhevskiy_kirill_14_123@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123123')
        driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.find_element(By.XPATH, '//button[contains(text(), "Оформить заказ")]').is_enabled()

    def test_login_with_login_button_on_reset_pw_page(self, driver, homepage):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.RESET_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.RES_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('chizhevskiy_kirill_14_123@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123123')
        driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.find_element(By.XPATH, '//button[contains(text(), "Оформить заказ")]').is_enabled()
