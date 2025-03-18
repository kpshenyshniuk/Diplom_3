from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    button_enter_register_page = (By.XPATH, '//p//following-sibling::a[@href="/login"]')  # локатор кнопки Войти на странице Регистрации
    name_field_registration_page = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Локатор поля Имя на странице регистрации
    email_field_registration_page = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Локатор поля Email на странице регистрации
    password_field_registration_page = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Локатор поля Пароль на странице регистрации
    register_button_registration_page = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка Зарегистрироваться на странице регистрации
    error_text_registration_page = (By.XPATH, '//p[@class="input__error text_type_main-default"]')  # Локатор текста с ошибкой при вводе не валидного пароля
