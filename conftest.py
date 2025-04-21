import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):  # выношу вход в систему в отдельный вспомогательный метод
    driver.get(Data.STELLAR_BURGERS_URL + "login")

    # заполнение поля "Email"
    email_field = WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.visibility_of_element_located(Locators.EMAIL_FIELD)
    )
    email_field.send_keys(Data.AUTH_EMAIL)

    # заполнение поля "Пароль"
    password_field = WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.visibility_of_element_located(Locators.PASSWORD_FIELD)
    )
    password_field.send_keys(Data.AUTH_PASSWORD)

    # нажатие кнопки "Войти"
    enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.element_to_be_clickable(Locators.ENTER_BUTTON)
    )
    enter_button.click()

    # ожидание перехода на главную страницу
    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.url_to_be(Data.STELLAR_BURGERS_URL)
    )


@pytest.fixture
def go_to_personal_account(driver):  # выношу переход в личный кабинет в отдельный вспомогательный метод

    # переход в личный кабинет
    personal_account_button = WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
    )
    personal_account_button.click()

    # ожидание перехода на страницу личный кабинет
    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.url_to_be(Data.STELLAR_BURGERS_URL + "account/profile")
    )
