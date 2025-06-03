import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import Data
from locators import Locators


class TestConstructor:

    def test_go_to_sauces_section(self, driver):  # проверка перехода к разделу «Соусы» (незалогиненым пользователем)
        # переход на главную страницу
        driver.get(Data.STELLAR_BURGERS_URL)

        # нажатие на кнопку "Соусы"
        sauces_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.SAUCES_SECTION))
        sauces_button.click()

        # ожидание, что раздел "Соусы" активен
        active_section = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION_SAUCES))

        # проверка, что раздел "Соусы" активен
        assert "Соусы" in active_section.text, "Раздел 'Соусы' не активен"

    def test_go_to_buns_section(self, driver):  # проверка перехода к разделу «Булки» (незалогиненым пользователем)
        # переход на главную страницу
        driver.get(Data.STELLAR_BURGERS_URL)

        # нажатие на кнопку "Булки"
        buns_button = WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.BUNS_SECTION))
        buns_button.click()

        # проверка, что раздел "Булки" активен
        active_section = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION_BUNS))
        assert "Булки" in active_section.text, "Раздел 'Булки' не активен"

    def test_go_to_fillings_section(self,
                                    driver):  # проверка перехода к разделу «Начинки» (незалогиненым пользователем)
        # переход на главную страницу
        driver.get(Data.STELLAR_BURGERS_URL)

        # нажатие на кнопку "Начинки"
        fillings_button = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(Locators.FILLINGS_SECTION))
        fillings_button.click()

        # ожидание, что раздел "Начинки" активен
        active_section = WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION_FILLINGS))

        # проверка, что активный раздел — "Начинки"
        assert "Начинки" in active_section.text, "Раздел 'Начинки' не активен"
