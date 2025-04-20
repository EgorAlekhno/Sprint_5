
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from data import Data
from locators import Locators
from fake_data import get_sign_up_data


class TestRegistration:  # класс для проверки регистрации

    def test_successful_registration(self, driver: WebDriver):  # проверяет успешную регистрацию пользователя
        # переход на страницу регистрации
        driver.get(Data.STELLAR_BURGERS_URL + "register")

        # генерация тестовых данных (email и пароль)
        email, password = get_sign_up_data()

        # ожидание появления поля "Имя" и ввод имени
        name_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.REGISTER_NAME_FIELD))
        name_field.send_keys("Egor Aliakhno")

        # ожидание появления поля "Email" и ввод email
        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.REGISTER_EMAIL_FIELD))
        email_field.send_keys(email)

        # ожидание появления поля "Пароль" и ввод пароля
        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.REGISTER_PASSWORD_FIELD))
        password_field.send_keys(password)

        # ожидание появления кнопки "Зарегистрироваться" и клик по ней
        register_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        register_button.click()

        # ожидание перехода на страницу входа после успешной регистрации
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_to_be(Data.STELLAR_BURGERS_URL + "login"))

        # проверка, что текущий URL соответствует странице входа
        assert driver.current_url == Data.STELLAR_BURGERS_URL + "login"

    def test_invalid_password_registration(self, driver: WebDriver):  # проверяет отображение сообщения об ошибке
        # при вводе некорректного пароля (менее 6 символов)

        # переход на страницу регистрации
        driver.get(Data.STELLAR_BURGERS_URL + "register")

        # генерация тестового email
        email, _ = get_sign_up_data()

        # ожидание появления поля "Имя" и ввод имени
        name_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.REGISTER_NAME_FIELD))
        name_field.send_keys("Egor Aliakhno")

        # ожидание появления поля "Email" и ввод email
        email_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.REGISTER_EMAIL_FIELD))
        email_field.send_keys(email)

        # ожидание появления поля "Пароль" и ввод некорректного пароля (менее 6 символов)
        password_field = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.REGISTER_PASSWORD_FIELD))
        password_field.send_keys("12345")  # Некорректный пароль

        # ожидание появления кнопки "Зарегистрироваться" и клик по ней
        register_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        register_button.click()

        # ожидание появления сообщения об ошибке
        error_message = WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR_MESSAGE))

        # проверка, что сообщение об ошибке отображается
        assert error_message.is_displayed(), "Сообщение об ошибке для пароля меньше 6-ти символов не отображается"
