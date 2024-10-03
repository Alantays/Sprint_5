import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import constants


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def authorization(driver):
    driver.get(constants.LOGIN_URL)
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.LOGIN_EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.LOGIN_PASSWORD)
    driver.find_element(*Locators.LOGIN_APPLY_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be(constants.HOMEPAGE_URL))
    return driver


@pytest.fixture(scope="function")
def homepage(driver):
    driver.get(constants.HOMEPAGE_URL)
    return driver
