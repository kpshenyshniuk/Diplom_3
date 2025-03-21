from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    input_new_password_reset_password_page = (By.XPATH, '//div[contains(@class, "input_type_password")]')
    input_code_reset_password_page = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')
    locator_overlay_reset_password_page = (By.XPATH, "//div[contains(@class, 'Modal_modal')][img[@alt='loading animation']]")
    new_password_field_reset_password_page = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]")
    show_hide_new_password_icon_reset_password_page = (By.XPATH, "//div/div[contains(@class, 'input__icon input__icon-action')]")
    header_restore_password = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    input_email_field_restore_password_page = (By.XPATH, '//label[text()="Email"]/following-sibling::input[@class="text input__textfield text_type_main-default"]')
    button_restore_password_restore_page = (By.XPATH, '//button[text()="Восстановить"]')
    button_enter_forgot_password_page = (By.XPATH, '//p//following-sibling::a[@href="/login"]')  # локатор кнопки Войти на странице Восстановления пароля
