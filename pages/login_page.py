import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Links


class LoginPage(BasePage):

    email_field_login_page = (
        By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Локатор для поля Email на логин странице
    password_field_login_page = (
        By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # Локатор для поля pawword на логин странице
    login_button_login_page = (By.XPATH, '//button[text()="Войти"]')  # Локатор кнопки Войти на логин странице
    button_restore_password = (By.XPATH, '//a[contains(@class, "Auth_link") and text()="Восстановить пароль"]')

    @allure.step("Авторизируем пользователя")
    def login(self, username, password):
        """Логин в систему"""
        self.send_keys(self.email_field_login_page, username)
        self.send_keys(self.password_field_login_page, password)
        self.wait_clickable(self.login_button_login_page)
        self.click(self.login_button_login_page)

    @allure.step("открываем страницу Логина ")
    def open_login_page(self):
        self.open(Links.link_login_page)

    @allure.step("Ожидаем присутствие кнопки 'Войти' ")
    def wait_login_page_present(self):
        self.wait_present(self.login_button_login_page)

    @allure.step("находим кнопку 'Войти' ")
    def find_login_button(self):
        return self.find_elements(self.login_button_login_page)

    @allure.step("Нажимаем на кнопку Восстановить пароль")
    def click_button_restore_password(self):
        element = self.wait_clickable(self.button_restore_password)
        self.script_click(element)
