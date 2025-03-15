from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from helpers import wait_clickable, wait_present, wait_visible, find_element, wait_invisible
from locators import LocatorsLoginPage, LocatorsMainPage, LocatorsProfilePage
from links import Links


class TestGetPages:
    def test_get_profile_page(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(user_data['user']['email'])
        find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(password)
        button = wait_visible(driver, LocatorsLoginPage.login_button_login_page)
        driver.execute_script("arguments[0].click();", button)
        wait_visible(driver, LocatorsMainPage.make_order_button)
        driver.get(Links.link_profile_page)
        wait_visible(driver, LocatorsProfilePage.exit_button_profile_page)
        email_field_value = find_element(driver, LocatorsProfilePage.email_field_profile_page).get_attribute(
            'value')
        assert email_field_value == user_data['user']['email']
        assert driver.current_url == Links.full_link_profile_page

    def test_get_order_history_page(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(user_data['user']['email'])
        find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(password)
        button = wait_visible(driver, LocatorsLoginPage.login_button_login_page)
        driver.execute_script("arguments[0].click();", button)
        wait_visible(driver, LocatorsMainPage.title_main_page)
        driver.get(Links.link_profile_page)
        button = wait_clickable(driver, LocatorsProfilePage.button_order_history)
        driver.execute_script("arguments[0].click();", button)

        assert driver.current_url == Links.order_history_link
        WebDriverWait(driver, 10).until(
            lambda d: "Account_link_active" in find_element(driver, LocatorsProfilePage.button_order_history).get_attribute("class"))

    def test_click_on_logout_button(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(user_data['user']['email'])
        find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(password)
        button = wait_visible(driver, LocatorsLoginPage.login_button_login_page)
        driver.execute_script("arguments[0].click();", button)
        wait_visible(driver, LocatorsMainPage.title_main_page)
        driver.get(Links.link_profile_page)
        button = wait_clickable(driver, LocatorsProfilePage.exit_button_profile_page)
        driver.execute_script("arguments[0].click();", button)
        wait_present(driver, LocatorsLoginPage.login_button_login_page)

        assert driver.current_url == Links.link_login_page
        assert find_element(driver, LocatorsLoginPage.login_button_login_page)
