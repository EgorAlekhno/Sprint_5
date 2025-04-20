from selenium.webdriver.common.by import By


class Locators:
    # локаторы для страницы регистрации
    REGISTER_NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # локатор для поля "Имя"
    REGISTER_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # локатор для поля "Email"
    REGISTER_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")  # локатор для поля "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # локатор для кнопки "Зарегистрироваться"
    PASSWORD_ERROR_MESSAGE = (
        By.XPATH, "//p[text()='Некорректный пароль']")  # сообщение об ошибке при некорректном пароле

    # локаторы для страницы логина
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # локатор для поля "Email"
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")  # локатор для поля "Пароль"
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")  # локатор для кнопки "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # локатор для кнопки "Войти в аккаунт"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # локатор для ссылки "Войти" !
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # локатор для кнопки "Выход"

    # локаторы для ЛК
    PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account']")  # локатор для кнопки "Личный Кабинет" !
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # локатор для логотипа "Stellar Burgers"

    # локаторы для раздела конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # локатор для кнопки "Конструктор"
    BUNS_SECTION = (By.XPATH, "//div[.//span[text()='Булки']]")  # локатор для кнопки "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")  # локатор для кнопки "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")  # локатор для кнопки "Начинки"
    ACTIVE_SECTION_BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']") # локатор для активного раздела булок
    ACTIVE_SECTION_SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Соусы']") # локатор для активного раздела соусов
    ACTIVE_SECTION_FILLINGS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Начинки']") # локатор для активного раздела наполнителей
