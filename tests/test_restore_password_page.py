import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import CommonData
from conftest import driver
from locators import Locators
from links import Links


class TestGetPages:

    def test_get_restore_password_page_by_restore_password_button(self, driver):
        driver.get(Links.link_login_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_restore_password))).click()

        assert driver.current_url == Links.link_forgot_password_page
        assert driver.find_element(By.XPATH, Locators.header_restore_password)

    def test_restore_password(self, driver, create_user):
        driver.get(Links.link_login_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_restore_password))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.input_email_field))).send_keys(create_user['user']['email'])
        time.sleep(4)
        assert driver.current_url == Links.link_forgot_password_page
        assert driver.find_element(By.XPATH, Locators.header_restore_password)