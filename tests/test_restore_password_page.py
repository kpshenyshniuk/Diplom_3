from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from urls import Links


class TestGetPages:

    def test_get_restore_password_page_by_restore_password_button(self, driver):
        login_page = LoginPage(driver)
        reset_page = ResetPasswordPage(driver)
        login_page.open(Links.link_login_page)
        button = login_page.wait_clickable(login_page.button_restore_password)
        driver.execute_script("arguments[0].click();", button)

        assert driver.current_url == Links.link_forgot_password_page
        assert reset_page.find_element(reset_page.header_restore_password)

    def test_restore_password(self, driver, create_user):
        login_page = LoginPage(driver)
        reset_page = ResetPasswordPage(driver)
        main_page = MainPage(driver)

        user_data, password = create_user
        main_page.open(Links.link_login_page)
        button = login_page.wait_clickable(login_page.button_restore_password)
        driver.execute_script("arguments[0].click();", button)
        reset_page.send_keys(reset_page.input_email_field_restore_password_page, user_data['user']['email'])
        button = login_page.wait_clickable(reset_page.button_restore_password_restore_page)
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 10).until(
            lambda d: "Modal_modal_opened" not in reset_page.find_element(reset_page.locator_overlay_reset_password_page).get_attribute("class"))

        assert driver.current_url == Links.reset_password_link
        assert reset_page.find_element(reset_page.input_new_password_reset_password_page)
        assert reset_page.find_element(reset_page.input_code_reset_password_page)

    def test_show_hide_button_underline_password_field(self, driver, create_user):
        login_page = LoginPage(driver)
        reset_page = ResetPasswordPage(driver)
        main_page = MainPage(driver)
        user_data, password = create_user
        main_page.open(Links.link_login_page)
        button = login_page.wait_clickable(login_page.button_restore_password)
        driver.execute_script("arguments[0].click();", button)
        reset_page.send_keys(reset_page.input_email_field_restore_password_page, user_data['user']['email'])
        button = login_page.wait_clickable(reset_page.button_restore_password_restore_page)
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 10).until(
            lambda d: "Modal_modal_opened" not in reset_page.find_element(
                reset_page.locator_overlay_reset_password_page).get_attribute("class"))
        state_before = reset_page.find_element(reset_page.new_password_field_reset_password_page).get_attribute("class")
        button = reset_page.find_element(reset_page.show_hide_new_password_icon_reset_password_page)
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 10).until(
            lambda d: 'input_status_active' in reset_page.find_element(reset_page.new_password_field_reset_password_page).get_attribute("class"))
        state_after = reset_page.find_element(reset_page.new_password_field_reset_password_page).get_attribute("class")

        assert 'input_status_active' not in state_before
        assert 'input_status_active' in state_after
