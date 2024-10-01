from selenium.webdriver.common.by import By


class Locators:
    # Главная страница
    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"
    )  # Кнопка "Личный кабинет"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт"
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # Кнопка "Оформить заказ"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип

    # Страница регистрации
    REG_NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")  # Поле ввода имени для регистрации
    REG_EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")  # Поле ввода email для регистрации
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода пароля для регистрации
    REG_APPLY_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение об ошибке пароля
    REG_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")  # Кнопка "Войти" на странице регистрации

    # Страница аутентификации
    LOGIN_PAGE_TITLE = (By.XPATH, "//h2[contains(text(),'Вход')]")  # Заголовок страницы входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # Поле ввода email для входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода пароля для входа
    LOGIN_APPLY_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка "Войти"
    REGISTRATION_BUTTON = (
        By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться" на странице входа
    RESET_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")  # Кнопка "Восстановить пароль"

    # Страница восстановления пароля
    RES_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")  # Кнопка "Войти" на странице восстановления пароля

    # Страница личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка "Выход"

    # Страница конструктора
    BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]")  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]")  # Раздел "Соусы"
    TOPPINGS_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]")  # Раздел "Начинки"
    BUNS_DIV = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div")  # Контейнер раздела "Булки"
    SAUCES_DIV = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div")  # Контейнер раздела "Соусы"
    TOPPINGS_DIV = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div")  # Контейнер раздела "Начинки"
