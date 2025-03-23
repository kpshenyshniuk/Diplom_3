import allure
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

    @allure.step("Находим заголовок Восстановление пароля")
    def find_header_restore_password(self):
        return self.find_element(self.header_restore_password)

    @allure.step("Вводим значение в поле email")
    def send_email_to_email_field(self, key):
        self.send_keys(self.input_email_field_restore_password_page, key)

    @allure.step("Делаем клик на кнопку Восстановить")
    def click_on_button_restore_password_restore_page(self):
        element = self.find_element(self.button_restore_password_restore_page)
        self.script_click(element)

    @allure.step("Ожидаем пока текст Modal_modal_opened пропадет из элемента overlay")
    def wait_text_in_locator_overlay_reset_password_page(self):
        self.wait_text_not_in_element_class(self.modal_opened, self.locator_overlay_reset_password_page)

    @allure.step("находим поле для ввода нового пароля Password")
    def find_input_new_password_reset_password_page(self):
        return self.find_element(self.input_new_password_reset_password_page)

    @allure.step("находим поле для ввода кода для восстановления пароля")
    def find_input_code_reset_password_page(self):
        return self.find_element(self.input_code_reset_password_page)

    @allure.step("Возвращаем имя класса поля ввода нового пароля Password")
    def get_new_password_field_reset_password_page_class(self):
        return self.get_element_class(self.new_password_field_reset_password_page)

    @allure.step("делаем клик на кнопка отобразить/скрыть пароль")
    def click_on_show_hide_new_password_icon_reset_password_page(self):
        element = self.find_element(self.show_hide_new_password_icon_reset_password_page)
        self.script_click(element)

    @allure.step("ожидаем текст active в поле для ввода нового пароля")
    def wait_text_in_new_password_field_reset_password_page(self):
        self.wait_text_in_element_class(self.input_status_active, self.new_password_field_reset_password_page)
