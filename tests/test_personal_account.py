import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver, login,
                                    go_to_personal_account):  # переход из личного кабинета по клику на кнопку «Личный кабинет»

        # проверка, что текущий URL соответствует странице личный кабинет
        assert driver.current_url == Data.STELLAR_BURGERS_URL + "account/profile"

    def test_go_to_constructor_from_personal_account(self, driver, login,
                                                     go_to_personal_account):  # переход из личного кабинета в конструктор
        # по клику на кнопку «Конструктор»

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

    def test_go_to_constructor_via_logo(self, driver, login,
                                        go_to_personal_account):  # проверяю переход из личного кабинета в конструктор
        # по клику на логотип Stellar Burger

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
