from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    ACC_ENTRANCE = [By.XPATH, "//button[text()='Войти в аккаунт']"] # кнопка Войти в аккаунт
    REG_LINK = [By.XPATH, "//a[text()='Зарегистрироваться']"] # ссылка Зарегистрироваться
    REG_NAME = [By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]"] # поле ввода Имя
    REG_EMAIL = [By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]"] # поле ввода Email
    REG_PASSWORD = [By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[3]"] # поле ввода Пароль
    REG_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"] # кнопка Зарегистрироваться
    ERROR_POPUP = [By.XPATH, "//p[text()='Некорректный пароль']"] # ошибка Некорректный пароль

    # Локаторы для входа
    # - вход по кнопке «Войти в аккаунт» на главной
    ACC_EMAIL = [By.XPATH, "//input[@type='text']"] # поле ввода Email
    ACC_PASSWORD = [By.XPATH, "//input[@type='password']"] # поле ввода Пароль
    ENTER = [By.XPATH, "//button[text()='Войти']"] # кнопка Войти в форме Войти в аккаунт
    # - вход через кнопку «Личный кабинет»
    PERSONAL_ACC = [By.XPATH, "//p[text()='Личный Кабинет']"] # кнопка Личный Кабинет
    # - вход через форму регистрации
    ENTER_REG_PAGE = [By.XPATH, "//a[text()='Войти']"] # ссылка Войти в форме регистрации
    # - вход через кнопку восстановление пароля
    RESET_PASS_LINK = [By.XPATH, "//a[text()='Восстановить пароль']"] # ссылка Восстановить пароль
    FORGOT_PASS_LINK = [By.XPATH, "//a[text()='Войти']"] # ссылка Войти на странице восстановления пароля

    # Переход из Личного кабинета
    # - по конструктору
    CONSTRUCTOR = [By.XPATH, "//p[text()='Конструктор']"] # кнопка Конструктор
    # - по логотипу Stellar Burgers
    SB_LOGO = [By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']"] # логотип Stellar Burgers
    # Выход из аккаунта
    EXIT_BUTTON = [By.XPATH, "//button[text()='Выход']"] # кнопка Выход

    # Раздел Конструктор
    BUNS = [By.XPATH, "//span[text()='Булки']"] # раздел Булки
    SAUSES = [By.XPATH, "//span[text()='Соусы']"] # раздел Соусы
    FILLINGS = [By.XPATH, "//span[text()='Начинки']"] # раздел Начинки







