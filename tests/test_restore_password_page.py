import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import CommonData
from conftest import driver
from locators import LocatorsLoginPage, LocatorsResetPasswordPage
from links import Links


class TestGetPages:

    def test_get_restore_password_page_by_restore_password_button(self, driver):
        driver.get(Links.link_login_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsLoginPage.button_restore_password))).click()

        assert driver.current_url == Links.link_forgot_password_page
        assert driver.find_element(By.XPATH, LocatorsResetPasswordPage.header_restore_password)

    def test_restore_password(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsLoginPage.button_restore_password))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsResetPasswordPage.input_email_field_restore_password_page))).send_keys(user_data['user']['email'])
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsResetPasswordPage.button_restore_password_restore_page))).click()
        WebDriverWait(driver, 10).until(
            lambda d: "Modal_modal_opened" not in d.find_element(By.XPATH, LocatorsResetPasswordPage.locator_overlay_reset_password_page).get_attribute("class"))

        assert driver.current_url == Links.reset_password_link
        assert driver.find_element(By.XPATH, LocatorsResetPasswordPage.input_new_password_reset_password_page)
        assert driver.find_element(By.XPATH, LocatorsResetPasswordPage.input_code_reset_password_page)

    def test_show_hide_button_underline_password_field(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsLoginPage.button_restore_password))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsResetPasswordPage.input_email_field_restore_password_page))).send_keys(
            user_data['user']['email'])
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, LocatorsResetPasswordPage.button_restore_password_restore_page))).click()
        WebDriverWait(driver, 10).until(
            lambda d: "Modal_modal_opened" not in d.find_element(By.XPATH, LocatorsResetPasswordPage.locator_overlay_reset_password_page).get_attribute(
                "class"))
        state_before = driver.find_element(By.XPATH, LocatorsResetPasswordPage.new_password_field_reset_password_page).get_attribute("class")
        driver.find_element(By.XPATH, LocatorsResetPasswordPage.show_hide_new_password_icon_reset_password_page).click()
        state_after = driver.find_element(By.XPATH, LocatorsResetPasswordPage.new_password_field_reset_password_page).get_attribute("class")

        assert 'input_status_active' not in state_before
        assert 'input_status_active' in state_after

