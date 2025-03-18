from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Локаторы
    email_field_login_page = (
        By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Локатор для поля Email на логин странице
    password_field_login_page = (
        By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # Локатор для поля pawword на логин странице
    login_button_login_page = (By.XPATH, '//button[text()="Войти"]')  # Локатор кнопки Войти на логин странице
    button_restore_password = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')

    def login(self, username, password):
        """Логин в систему"""
        self.send_keys(self.email_field_login_page, username)
        self.send_keys(self.password_field_login_page, password)
        self.click(self.login_button_login_page)
