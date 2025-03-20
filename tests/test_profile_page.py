from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import Links


class TestGetPages:
    def test_get_profile_page(self, driver, create_user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        user_data, password = create_user
        main_page.open(Links.link_login_page)
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visible(main_page.make_order_button)
        main_page.open(Links.link_profile_page)
        profile_page.wait_visible(profile_page.exit_button_profile_page)
        email_field_value = profile_page.find_element(profile_page.email_field_profile_page).get_attribute('value')
        assert email_field_value == user_data['user']['email']
        assert driver.current_url == Links.full_link_profile_page

    def test_get_order_history_page(self, driver, create_user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        user_data, password = create_user
        main_page.open(Links.link_login_page)
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visible(main_page.make_order_button)
        main_page.open(Links.link_profile_page)
        button = profile_page.wait_clickable(profile_page.button_order_history)
        driver.execute_script("arguments[0].click();", button)

        assert driver.current_url == Links.order_history_link
        WebDriverWait(driver, 10).until(
            lambda d: "Account_link_active" in profile_page.find_element(profile_page.button_order_history).get_attribute("class"))

    def test_click_on_logout_button(self, driver, create_user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        user_data, password = create_user
        main_page.open(Links.link_login_page)
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visible(main_page.make_order_button)
        main_page.open(Links.link_profile_page)
        button = profile_page.wait_clickable(profile_page.exit_button_profile_page)
        driver.execute_script("arguments[0].click();", button)
        login_page.wait_present(login_page.login_button_login_page)

        assert driver.current_url == Links.link_login_page
        assert login_page.find_elements(login_page.login_button_login_page)
