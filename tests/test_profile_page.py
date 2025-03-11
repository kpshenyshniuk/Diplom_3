import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import CommonData
from conftest import driver
from locators import Locators
from links import Links
from selenium.webdriver.common.action_chains import ActionChains



class TestGetPages:
    def test_get_profile_page(self, driver):
        driver.get(Links.link_login_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.email_field_login_page)))
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(
            CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(
            CommonData.valid_password)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.login_button_login_page)))
        driver.find_element(By.XPATH, Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.make_order_button)))
        driver.get(Links.link_profile_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.exit_button_profile_page)))
        email_field_value = driver.find_element(By.XPATH, Locators.email_field_profile_page).get_attribute(
            'value')
        assert email_field_value == CommonData.valid_email
        assert driver.current_url == Links.full_link_profile_page

    def test_get_order_history_page(self, driver):
        driver.get(Links.link_login_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.email_field_login_page)))
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(
            CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(
            CommonData.valid_password)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_profile_page))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_order_history))).click()
        assert driver.current_url == Links.order_history_link
        WebDriverWait(driver, 10).until(
            lambda d: "Account_link_active" in d.find_element(By.XPATH, Locators.button_order_history).get_attribute("class")
        )


    def test_click_on_logout_button(self, driver):
        driver.get(Links.link_login_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.email_field_login_page)))
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(
            CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(
            CommonData.valid_password)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_profile_page))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_profile_page))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.exit_button_profile_page))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.login_button_login_page)))

        assert driver.current_url == Links.link_login_page
        assert driver.find_element(By.XPATH, Locators.login_button_login_page)
