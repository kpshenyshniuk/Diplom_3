import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


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
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_login_page))
        self.click(self.login_button_login_page)
