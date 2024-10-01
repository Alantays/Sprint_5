from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestRegistration:

    def test_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys('Кирилл')
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys('chizhevskiy_kirill_14_723@yandex.ru')
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys('123123')
        driver.find_element(*Locators.REG_APPLY_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.LOGIN_PAGE_TITLE))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"