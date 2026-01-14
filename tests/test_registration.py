from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, LoginPage, RegistrationPage
from utils.generator import UserDataGenerator
from utils.user import TestUser
from utils.waiters import Waiter
from utils.constants import Constants

class TestRegistration:
    def test_registration_valid_user(self, driver):
        # Переход на страницу регистрации
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        # Ожидание открытия формы для входа
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPage.LOGIN_TITLE)
            )
        driver.find_element(*LoginPage.NO_ACCOUNT_BUTTON).click()
        # Ожидание загрузски страницы регистрации
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.REGISTRATION_TITLE)
            )
        # Ввод валидных данных для регистрации
        driver.find_element(*LoginPage.EMAIL).send_keys(UserDataGenerator.generate_valid_email())
        correct_password = UserDataGenerator.generate_valid_password()
        driver.find_element(*LoginPage.PASSWORD).send_keys(correct_password)
        driver.find_element(*RegistrationPage.REPEAT_PASSWORD).send_keys(correct_password)
        # Нажатие кнопки "Создать аккаунт"
        driver.find_element(*RegistrationPage.CREATE_ACCOUNT_BUTTON).click()
        # Ожидание перехода на главную страницу после успешной регистрации
        avatar_logo = WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(MainPage.AVATAR_LOGO)
            )
        # Проверка, что логотип аватара отображается
        assert avatar_logo.is_displayed()
        user_element = driver.find_element(*MainPage.USER)
        # Проверка, что имя пользователя и логотип аватара отображаются
        assert user_element.is_displayed() and user_element.text == "User."

    def test_registration_invalid_email(self, driver):
        # Переход на страницу регистрации
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        # Ожидание открытия формы для входа
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPage.LOGIN_TITLE)
            )
        driver.find_element(*LoginPage.NO_ACCOUNT_BUTTON).click()
        # Ожидание загрузки страницы регистрации
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.REGISTRATION_TITLE)
            )
        # Ввод невалидных данных для регистрации
        driver.find_element(*LoginPage.EMAIL).send_keys(UserDataGenerator.generate_invalid_email())
        correct_password = UserDataGenerator.generate_valid_password()
        driver.find_element(*LoginPage.PASSWORD).send_keys(correct_password)
        driver.find_element(*RegistrationPage.REPEAT_PASSWORD).send_keys(correct_password)
        # Нажатие кнопки "Создать аккаунт"
        driver.find_element(*RegistrationPage.CREATE_ACCOUNT_BUTTON).click()
        # Ожидание отображения ошибки при вводе невалидного email
        error_el = WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.ERROR_MESSAGE)
            )
        # Проверка на отображение сообщения об ошибке
        error_text = error_el.is_displayed() and error_el.text == Constants.ERROR_LABEL
        assert error_text
        # Проверка на подсветку 3 полей красным цветом
        error_fields_red = all([
            driver.find_element(*RegistrationPage.EMAIL_ERROR).is_displayed(),
            driver.find_element(*RegistrationPage.PASSWORD_ERROR).is_displayed(),
            driver.find_element(*RegistrationPage.REPEAT_PASSWORD_ERROR).is_displayed()
        ])
        assert error_fields_red

    def test_registration_existing_user(self, driver):
        # Переход на страницу регистрации
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        # Ожидание открытия формы для входа
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPage.LOGIN_TITLE)
            )
        driver.find_element(*LoginPage.NO_ACCOUNT_BUTTON).click()
        # Ожидание загрузски страницы регистрации
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.REGISTRATION_TITLE)
            )
            # Ввод данных для регистрации уже существующего пользователя
        driver.find_element(*LoginPage.EMAIL).send_keys(TestUser.EMAIL)
        driver.find_element(*LoginPage.PASSWORD).send_keys(TestUser.PASSWORD)
        driver.find_element(*RegistrationPage.REPEAT_PASSWORD).send_keys(TestUser.PASSWORD)
         # Нажатие кнопки "Создать аккаунт"
        driver.find_element(*RegistrationPage.CREATE_ACCOUNT_BUTTON).click()
        # Ожидание отображения ошибки при вводе невалидного email
        error_el = WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.ERROR_MESSAGE)
            )
        # Проверка на отображение сообщения об ошибке
        error_text = error_el.is_displayed() and error_el.text == Constants.ERROR_LABEL
        assert error_text
        # Проверка на подсветку 3 полей красным цветом
        error_fields_red = all([
            driver.find_element(*RegistrationPage.EMAIL_ERROR).is_displayed(),
            driver.find_element(*RegistrationPage.PASSWORD_ERROR).is_displayed(),
            driver.find_element(*RegistrationPage.REPEAT_PASSWORD_ERROR).is_displayed()
        ])
        assert error_fields_red

        