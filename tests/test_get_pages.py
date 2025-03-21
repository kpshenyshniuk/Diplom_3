import allure
from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage
from urls import Links


class TestGetPages:

    @allure.title("Тест перехода на страницу Профиля пользователя")
    def test_get_profile_page(self, driver, create_user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visible_make_order_button()
        profile_page.open_profile_page()
        profile_page.wait_visible_exit_button_profile_page()
        email_field_value = profile_page.get_class_email_field()

        assert email_field_value == user_data['user']['email']
        assert profile_page.is_profile_page_opened()

    @allure.title("Тест перехода на страницу История заказов")
    def test_get_order_history_page(self, driver, create_user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        order_page = OrderHistoryPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visible_make_order_button()
        profile_page.open_profile_page()
        profile_page.click_on_button_order_history()
        profile_page.wait_text_in_button_order_history()

        assert order_page.is_order_history_page_opened()

    @allure.title("Тест нажатие на кнопку Выйти")
    def test_click_on_logout_button(self, driver, create_user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visible_make_order_button()
        profile_page.open_profile_page()
        profile_page.click_on_exit_button()
        login_page.wait_login_page_present()

        assert login_page.is_login_page_opened()
        assert login_page.find_login_button()
