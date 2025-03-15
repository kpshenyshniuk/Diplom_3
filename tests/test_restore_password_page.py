from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from helpers import wait_clickable, find_element
from locators import LocatorsLoginPage, LocatorsResetPasswordPage
from links import Links


class TestGetPages:

    def test_get_restore_password_page_by_restore_password_button(self, driver):
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.button_restore_password).click()

        assert driver.current_url == Links.link_forgot_password_page
        assert find_element(driver, LocatorsResetPasswordPage.header_restore_password)

    def test_restore_password(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.button_restore_password).click()
        wait_clickable(driver, LocatorsResetPasswordPage.input_email_field_restore_password_page).send_keys(user_data['user']['email'])
        wait_clickable(driver, LocatorsResetPasswordPage.button_restore_password_restore_page).click()
        WebDriverWait(driver, 10).until(
            lambda d: "Modal_modal_opened" not in find_element(driver, LocatorsResetPasswordPage.locator_overlay_reset_password_page).get_attribute("class"))

        assert driver.current_url == Links.reset_password_link
        assert find_element(driver, LocatorsResetPasswordPage.input_new_password_reset_password_page)
        assert find_element(driver, LocatorsResetPasswordPage.input_code_reset_password_page)

    def test_show_hide_button_underline_password_field(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        button = wait_clickable(driver, LocatorsLoginPage.button_restore_password)
        driver.execute_script("arguments[0].click();", button)
        wait_clickable(driver, LocatorsResetPasswordPage.input_email_field_restore_password_page).send_keys(
            user_data['user']['email'])
        button = wait_clickable(driver, LocatorsResetPasswordPage.button_restore_password_restore_page)
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 10).until(
            lambda d: "opened" not in find_element(driver, LocatorsResetPasswordPage.locator_overlay_reset_password_page).get_attribute(
                "class"))
        state_before = find_element(driver, LocatorsResetPasswordPage.new_password_field_reset_password_page).get_attribute("class")
        button = find_element(driver, LocatorsResetPasswordPage.show_hide_new_password_icon_reset_password_page)
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 10).until(
            lambda d: 'input_status_active' in find_element(driver, LocatorsResetPasswordPage.new_password_field_reset_password_page).get_attribute("class"))
        state_after = find_element(driver, LocatorsResetPasswordPage.new_password_field_reset_password_page).get_attribute("class")

        assert 'input_status_active' not in state_before
        assert 'input_status_active' in state_after
