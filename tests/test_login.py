from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, LoginPage
from utils.user import TestUser
from utils.waiters import Waiter


class TestLogin:
    def test_login_valid_user(self, driver):
        # Переход на страницу входа
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        # Ожидание открытия формы для входа
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPage.LOGIN_TITLE)
            )
        # Ввод валидных данных для входа
        driver.find_element(*LoginPage.EMAIL).send_keys(TestUser.EMAIL)
        driver.find_element(*LoginPage.PASSWORD).send_keys(TestUser.PASSWORD)
        # Нажатие кнопки войти 
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        # Проверка успешного входа на главную страницу, логотип и аватар отображаюся
        assert WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(MainPage.AVATAR_LOGO)
        )
        assert WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(MainPage.USER)).text == "User."