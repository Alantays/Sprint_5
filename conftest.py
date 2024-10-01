import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def authorization(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('chizhevskiy_kirill_14_123@yandex.ru')
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123123')
    driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    return driver


@pytest.fixture(scope="function")
def homepage(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    return driver
