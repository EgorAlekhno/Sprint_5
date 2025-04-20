import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestPersonalAccount:

    def login(self, driver):  # выношу вход в систему в отдельный вспомогательный метод
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

    def go_to_personal_account(self, driver):  # выношу переход в личный кабинет в отдельный вспомогательный метод

        # переход в личный кабинет
        personal_account_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
        )
        personal_account_button.click()

        # ожидание перехода на страницу личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "account/profile")
        )

    def test_go_to_personal_account(self, driver):  # переход из личного кабинета по клику на кнопку «Личный кабинет»
        self.login(driver)  # вход в систему
        self.go_to_personal_account(driver)  # переход в личный кабинет

        # проверка, что текущий URL соответствует странице личный кабинет
        assert driver.current_url == Data.STELLAR_BURGERS_URL + "account/profile"

    def test_go_to_constructor_from_personal_account(self, driver):  # переход из личного кабинета в конструктор
        # по клику на кнопку «Конструктор»

        self.login(driver)  # вход в систему
        self.go_to_personal_account(driver)  # переход в личный кабинет

        # нажатие на кнопку "Конструктор"
        constructor_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        # проверка, что текущий URL соответствует главной странице
        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_go_to_constructor_via_logo(self, driver):  # проверяю переход из личный кабинет в конструктор
        # по клику на логотип Stellar Burger

        self.login(driver)  # вход в систему
        self.go_to_personal_account(driver)  # переход в личный кабинет

        # Нажатие на логотип Stellar Burgers
        logo_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.LOGO_BUTTON)
        )
        logo_button.click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL)
        )

        # проверка, что текущий URL соответствует главной странице
        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_logout(self, driver):  # проверяю выход из аккаунта по кнопке «Выйти» в личный кабинет

        self.login(driver)  # вход в систему
        self.go_to_personal_account(driver)  # переход в личный кабинет

        # нажатие на кнопку "Выйти"
        logout_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()

        # ожидание перехода на страницу входа
        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.url_to_be(Data.STELLAR_BURGERS_URL + "login")
        )

        # проверка, что текущий URL соответствует странице входа
        assert driver.current_url == Data.STELLAR_BURGERS_URL + "login"
