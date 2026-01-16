from selenium.webdriver.common.by import By


class MainPage:
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Вход и регистрация')]"
    )
    CREATION_BUTTON = (
        By.XPATH,
        "//button[text() = 'Разместить объявление']"
    )
    USER = (
        By.CSS_SELECTOR,
        "h3.profileText.name"
    )
    AVATAR_LOGO = (
        By.CSS_SELECTOR,
        "button.circleSmall"
    )
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text() = 'Выйти']"
    )


class LoginPage:
    LOGIN_TITLE = (
        By.XPATH,
        "//h1[text() = 'Войти']"
    )
    EMAIL = (
        By.NAME,
        "email"
    )
    PASSWORD = (
        By.NAME,
        "password"
    )
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type = 'submit' and contains(@class, 'buttonPrimary') and text() = 'Войти']"
    )
    NO_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[text() = 'Нет аккаунта']"
    )


class RegistrationPage:
    REGISTRATION_TITLE = (
        By.XPATH,
        "//h1[text() = 'Зарегистрироваться']"
    )
    REPEAT_PASSWORD = (
        By.NAME,
        "submitPassword"
    )
    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[@type ='submit' and contains(@class, 'buttonPrimary') and text() = 'Создать аккаунт']"
    )
    EMAIL_ERROR = (
        By.CSS_SELECTOR,
        "div[class*=input_inputError] input[name='email']"
    )
    PASSWORD_ERROR = (
        By.CSS_SELECTOR,
        "div[class*=input_inputError] input[name='password']"
    )
    REPEAT_PASSWORD_ERROR = (
        By.CSS_SELECTOR,
        "div[class*=input_inputError] input[name='submitPassword']"
    )
    ERROR_MESSAGE = (
        By.XPATH, "//span[contains(@class, 'input_span') and text() = 'Ошибка']"
    )


class CreationPage:
    CREATION_TITLE = (
        By.XPATH,
        "//h1[text() = 'Новое объявление']"
    )
    UNAUTHORIZED_CREATION_TITLE = (
        By.XPATH,
        "//h1[text() = 'Чтобы разместить объявление, авторизуйтесь']"
    )
    AD_TITLE = (
        By.NAME,
        "name"
    )
    AD_DESCRIPTION = (
        By.CSS_SELECTOR,
        "textarea[name='description']"
    )
    AD_PRICE = (
        By.NAME,
        "price"
    )
    PUBLISH_BUTTON = (
        By.XPATH,
        "//button[text() = 'Опубликовать']"
    )


class DropDown:
    CATEGORY = (
        By.CSS_SELECTOR,
        "div[class*='dropDownMenu_input'] input[name='category'] + button"
    )
    CITY = (
        By.CSS_SELECTOR,
        "div[class*='dropDownMenu_input'] input[name='city'] + button"
    )
    CATEGORY_OPTION = (
        By.XPATH,
        "//button[.//span[text() = 'Авто']]"
    )
    CITY_OPTION = (
        By.XPATH,
        "//button[.//span[text() = 'Москва']]"
    )


class RadioButton:
    CONDITION_NEW = (
        By.XPATH,
        "//label[text()='Новый']"
    )
    CONDITION_USED = (
        By.XPATH,
        "//label[text()='Б/У']"
    )


class ProfilePage:
    PROFILE_TITLE = (
        By.XPATH,
        "//h1[text() = 'Мой профиль']"
    )
    MY_ADS = (
        By.XPATH,
        "//h1[text() = 'Мои объявления']"
    )
    CARD_ADD = (
        By.CSS_SELECTOR,
        "div[class*='grid_threeColumns'] div.card"
    )