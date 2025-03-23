import allure
from conftest import driver
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage


class TestOrderHistoryPage:

    @allure.title("Тест нажатие на сделанный заказ на странице Лента заказов")
    def test_click_on_order(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.login(user_data['user']['email'], password)
        main_page.make_order()
        main_page.click_button_close_popup()
        main_page.click_button_feed()
        feed_page.click_first_order()
        feed_page.wait_text_in_details_section()
        element = feed_page.get_order_number_details_screen()

        assert element.is_displayed()

    @allure.title("Тест заказы со страницы История заказов также отображаются на страниже Лента заказов")
    def test_orders_from_history_page_shown_on_feed_page(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        feed_page = FeedPage(driver)
        order_history_page = OrderHistoryPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.login(user_data['user']['email'], password)
        main_page.make_order()
        main_page.click_button_close_popup()
        main_page.click_profile_button()
        profile_page.click_on_button_order_history()
        main_page.wait_present(profile_page.first_order_number)
        order_number_history = order_history_page.get_first_order_number_text()
        main_page.click_button_feed()
        feed_page.wait_present_ul_locator()
        feed_page.wait_visible_list_items()
        feed_page.wait_visible_order_number_history_in_text_in_list(order_number_history)
        orders_in_feed = [item.text for item in feed_page.get_text_in_list()]

        assert order_number_history in orders_in_feed

    @allure.title("Тест счетчик всех заказов увеличивается после сделанного заказа")
    def test_all_orders_counter_increase(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visibility_title()
        feed_page.open_feed_page()
        count_before = feed_page.get_all_order_count()
        main_page.open_main_page()
        main_page.make_order()
        main_page.click_button_close_popup()
        feed_page.open_feed_page()
        feed_page.wait_all_count_increase(count_before)
        count_after = feed_page.get_all_order_count()

        assert int(count_before) == int(count_after) - 1

    @allure.title("Тест счетчик заказов за сегодня увеличивается после сделанного заказа")
    def test_today_orders_counter_increase(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visibility_title()
        feed_page.open_feed_page()
        count_before = feed_page.get_today_order_count()
        main_page.open_main_page()
        main_page.make_order()
        main_page.click_button_close_popup()
        feed_page.open_feed_page()
        feed_page.wait_today_count_increase(count_before)
        count_after = feed_page.get_today_order_count()

        assert int(count_before) == int(count_after) - 1

    @allure.title("Тест отображается корректный номер заказа в поле 'В работе'")
    def test_correct_number_shown_in_work(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visibility_title()
        main_page.open_main_page()
        main_page.make_order()
        order_number = main_page.get_new_order_number_text()
        main_page.click_button_close_popup()
        feed_page.open_feed_page()
        feed_page.wait_text_in_order_number_in_work(order_number)
        order_number_in_work = feed_page.get_order_number_in_work()

        assert order_number in order_number_in_work
