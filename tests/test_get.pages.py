import allure
from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import Links


class TestGetPages:

    @allure.title("Тест перехода на страницу Профиля пользователя")
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

    @allure.title("Тест перехода на страницу История заказов")
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
        main_page.script_click(button)
        main_page.wait_text_in_element_class(main_page.account_link_active, profile_page.button_order_history)

        assert driver.current_url == Links.order_history_link

    @allure.title("Тест нажатие на кнопку Выйти")
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
        main_page.script_click(button)
        login_page.wait_present(login_page.login_button_login_page)

        assert driver.current_url == Links.link_login_page
        assert login_page.find_elements(login_page.login_button_login_page)
