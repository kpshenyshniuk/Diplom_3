from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    input_new_password_reset_password_page = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div')
    input_code_reset_password_page = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div')
    locator_overlay_reset_password_page = (By.XPATH, "//*[@id='root']/div/div")
    new_password_field_reset_password_page = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div')
    show_hide_new_password_icon_reset_password_page = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/div')
    header_restore_password = (By.XPATH, '//*[@id="root"]/div/main/div/h2')
    input_email_field_restore_password_page = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset/div/div/input')
    button_restore_password_restore_page = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    button_enter_forgot_password_page = (By.XPATH, '//p//following-sibling::a[@href="/login"]')  # локатор кнопки Войти на странице Восстановления пароля
