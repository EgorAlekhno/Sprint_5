import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestLogoutFromPersonalAccount:

    def test_logout(self, driver, login,
                    go_to_personal_account):  # проверяю выход из аккаунта по кнопке «Выйти» в личный кабинет

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
