import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPage, LoginPage
from utils.user import TestUser
from utils.waiters import Waiter
from utils.urls import Urls


# Фикстура для инициализации веб-драйвера
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


# Фикстура для входа на сайт
@pytest.fixture
def login_user(driver):
    # Ожидаем загрузки главной страницы
    WebDriverWait(
        driver, Waiter.DEFAULT_WAIT_TIME).until(
        EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)
    )
    # Выполняем вход на сайт с использованием тестового пользователя
    driver.find_element(*MainPage.LOGIN_BUTTON).click()
    driver.find_element(*LoginPage.EMAIL).send_keys(TestUser.EMAIL)
    driver.find_element(*LoginPage.PASSWORD).send_keys(TestUser.PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()
    # Ожидаем, пока пользователь войдет в систему 
    WebDriverWait(
        driver, Waiter.DEFAULT_WAIT_TIME).until(
        EC.visibility_of_element_located(MainPage.AVATAR_LOGO)
        )
    return driver