from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, CreationPage, DropDown, RadioButton, ProfilePage
from utils.waiters import Waiter
from utils.constants import Constants

class TestCreationAd:
    def test_creation_ad_unauthorized_user(self, driver: WebDriver):
        # Нажатие на кнопку создания объявления
        driver.find_element(*MainPage.CREATION_BUTTON).click()
        # Ожидание открытия формы для создания объявления
        creation_form = WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(CreationPage.UNAUTHORIZED_CREATION_TITLE)
            )
        assert creation_form.is_displayed() and creation_form.text == Constants.AUTH_REQUIRED_LABEL

    def test_creation_ad_authorized_user(self, login_user):
        driver = login_user
        # Нажатие на кнопку создания объявления
        driver.find_element(*MainPage.CREATION_BUTTON).click()
        # Ожидание открытия формы для создания объявления
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(CreationPage.CREATION_TITLE)
            )
        # Ввод данных для создания объявления
        driver.find_element(*CreationPage.AD_TITLE).send_keys(Constants.TEST_TITLE)
        driver.find_element(*CreationPage.AD_DESCRIPTION).send_keys(Constants.TEST_PRODUCT_DESCRIPTION)
        driver.find_element(*CreationPage.AD_PRICE).send_keys(str(Constants.TEST_PRICE))
        # Выбор категории из выпадающего списка
        driver.find_element(*DropDown.CATEGORY).click()
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(DropDown.CATEGORY_OPTION)
            )
        driver.find_element(*DropDown.CATEGORY_OPTION).click()
        # Выбор города из выпадающего списка
        driver.find_element(*DropDown.CITY).click()
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(DropDown.CITY_OPTION)
            )
        driver.find_element(*DropDown.CITY_OPTION).click()
        # Выбор состояния товара с помощью радиокнопок
        driver.find_element(*RadioButton.CONDITION_USED).click()
        # Нажатие кнопки "Опубликовать"
        driver.find_element(*CreationPage.PUBLISH_BUTTON).click()
        # Ожидание перехода на главную страницу после создания объявления
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until( 
            EC.visibility_of_element_located(MainPage.AVATAR_LOGO) 
            )
        # Переход в профиль пользователя
        driver.find_element(*MainPage.AVATAR_LOGO).click()
        # Ожидание перехода на страницу профиля
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ProfilePage.PROFILE_TITLE) 
            )
        # Ожидание появления надписи "Мои объявления"
        WebDriverWait(
            driver, Waiter.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ProfilePage.MY_ADS)
            )
        # Ожидание появления созданного объявления в списке
        card_ad = WebDriverWait( 
            driver, Waiter.DEFAULT_WAIT_TIME).until( 
            EC.visibility_of_element_located(ProfilePage.CARD_ADD) 
            ) 
        assert card_ad.is_displayed()


    