from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, LoginPage
from utils.user import TestUser
from utils.waiters import Waiter

class TestLogout:
    def test_logout_user(self, login_user):
        # Используем фикстура для авторизации пользователя
        driver = login_user
        # Нажатие кнопки выйти
        driver.find_element(*MainPage.LOGOUT_BUTTON).click()
        # Проверка успешного выхода в неавтаризованное состояние
        login_button = WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(MainPage.LOGIN_BUTTON)
            )
        # Проверка, что отображается кнопка входа
        assert login_button.is_displayed()
        # Проверка, что аватарка пользователя не отображается
        assert WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
                EC.invisibility_of_element_located(MainPage.AVATAR_LOGO)
            )
        # Проверка, что имя пользователя не отображается
        assert WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
                EC.invisibility_of_element_located(MainPage.USER)
            )