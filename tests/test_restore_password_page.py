import allure
from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from urls import Links


class TestRestorePasswordPage:

    @allure.title("Тест переход на страницу восстановление пароля через кнопку Восстановить пароль")
    def test_get_restore_password_page_by_restore_password_button(self, driver):
        login_page = LoginPage(driver)
        reset_page = ResetPasswordPage(driver)
        login_page.open_login_page()
        login_page.click_button_restore_password()

        assert reset_page.get_current_url == Links.link_forgot_password_page
        assert reset_page.find_header_restore_password()

    @allure.title("Тест восстановление пароля")
    def test_restore_password(self, driver, create_user):
        login_page = LoginPage(driver)
        reset_page = ResetPasswordPage(driver)
        main_page = MainPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.click_button_restore_password()
        reset_page.send_email_to_email_field(user_data['user']['email'])
        reset_page.click_on_button_restore_password_restore_page()
        reset_page.wait_text_in_locator_overlay_reset_password_page()

        assert reset_page.get_current_url == Links.reset_password_link
        assert reset_page.find_input_new_password_reset_password_page()
        assert reset_page.find_input_code_reset_password_page()

    @allure.title("Тест при нажатии на кнопку скрыть отобразить пароль, поле становиться выбранным и подсвечивается")
    def test_show_hide_button_underline_password_field(self, driver, create_user):
        login_page = LoginPage(driver)
        reset_page = ResetPasswordPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.click_button_restore_password()
        reset_page.send_email_to_email_field(user_data['user']['email'])
        reset_page.click_on_button_restore_password_restore_page()
        reset_page.wait_text_in_locator_overlay_reset_password_page()
        state_before = reset_page.get_new_password_field_reset_password_page_class()
        reset_page.click_on_show_hide_new_password_icon_reset_password_page()
        reset_page.wait_text_in_new_password_field_reset_password_page()
        state_after = reset_page.get_new_password_field_reset_password_page_class()

        assert reset_page.input_status_active not in state_before
        assert reset_page.input_status_active in state_after
