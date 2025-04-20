import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import Data
from locators import Locators


class TestLogin:  # новый класс для проверки входа в систему

    def test_login_via_main_page(self, driver):  # вход через кнопку "Войти в аккаунт" на главной странице
        driver.get(Data.STELLAR_BURGERS_URL)  # переход на главную страницу

        # нажатие кнопки "Войти в аккаунт" и ожидание
        login_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        login_button.click()

        # ожидание перехода на страницу входа
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_to_be(Data.STELLAR_BURGERS_URL + "login"))

        # заполнение поля "Email"
        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        email_field.send_keys(Data.AUTH_EMAIL)

        # заполнение поля "Пароль"
        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD))
        password_field.send_keys(Data.AUTH_PASSWORD)

        # нажатие кнопки "Войти"
        enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
        enter_button.click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_to_be(Data.STELLAR_BURGERS_URL))

        # проверка, что текущий URL соответствует главной странице
        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_login_via_personal_account_button(self, driver):  # вход через кнопку "Личный кабинет"
        driver.get(Data.STELLAR_BURGERS_URL)  # переход на главную страницу

        # нажатие кнопки "Личный кабинет" и ожидание
        personal_account_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT))
        personal_account_button.click()

        # ожидание перехода на страницу логина
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_to_be(Data.STELLAR_BURGERS_URL + "login"))

        # заполнение поля "Email"
        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        email_field.send_keys(Data.AUTH_EMAIL)


        # заполнение поля "Пароль"
        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD))
        password_field.send_keys(Data.AUTH_PASSWORD)

        # нажатие кнопки "Войти"
        enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
        enter_button.click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_to_be(Data.STELLAR_BURGERS_URL))

        # проверка, что текущий URL соответствует главной странице
        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_login_via_registration_form(self, driver):  # вход через кнопку в форме регистрации
        driver.get(Data.STELLAR_BURGERS_URL + "register")  # переход на страницу регистрации

        # нажатие кнопки "Войти" в форме регистрации
        login_link = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.LOGIN_LINK))
        login_link.click()

        # ожидание перехода на страницу логина
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_to_be(Data.STELLAR_BURGERS_URL + "login"))

        # заполнение поля "Email"
        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        email_field.send_keys(Data.AUTH_EMAIL)

        # заполнение поля "Пароль"
        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD))
        password_field.send_keys(Data.AUTH_PASSWORD)

        # нажатие кнопки "Войти"
        enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
        enter_button.click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_to_be(Data.STELLAR_BURGERS_URL))

        # проверка, что текущий URL соответствует главной странице
        assert driver.current_url == Data.STELLAR_BURGERS_URL

    def test_login_via_password_recovery_form(self, driver):  # вход через кнопку в форме восстановления пароля
        driver.get(Data.STELLAR_BURGERS_URL + "forgot-password")  # переход на страницу восстановления пароля

        # нажатие кнопки "Войти" в форме восстановления пароля
        login_link = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.LOGIN_LINK))
        login_link.click()

        # ожидание перехода на страницу логина
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_to_be(Data.STELLAR_BURGERS_URL + "login"))

        # заполнение поля "Email"
        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        email_field.send_keys(Data.AUTH_EMAIL)

        # заполнение поля "Пароль"
        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD))
        password_field.send_keys(Data.AUTH_PASSWORD)

        # нажатие кнопки "Войти"
        enter_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
        enter_button.click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_to_be(Data.STELLAR_BURGERS_URL))

        # проверка, что текущий URL соответствует главной странице
        assert driver.current_url == Data.STELLAR_BURGERS_URL
