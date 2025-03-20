import allure
from conftest import driver
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import Links


class TestOrderHistoryPage:

    @allure.title("Тест нажатие на сделанный заказ на странице Лента заказов")
    def test_click_on_order(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        user_data, password = create_user
        main_page.open(Links.link_login_page)
        login_page.login(user_data['user']['email'], password)
        main_page.make_order()
        button = main_page.find_element(main_page.button_close_popup)
        main_page.script_click(button)
        button = main_page.find_element(main_page.button_feed)
        main_page.script_click(button)
        button = main_page.wait_visible(feed_page.first_order)
        button.click()
        main_page.wait_text_in_element_class(feed_page.text_opened, feed_page.details_section)
        element = main_page.wait_visible(feed_page.order_number_details_screen)

        assert element.is_displayed()

    @allure.title("Тест заказы со страницы История заказов также отображаются на страниже Лента заказов")
    def test_orders_from_history_page_shown_on_feed_page(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        feed_page = FeedPage(driver)
        user_data, password = create_user
        main_page.open(Links.link_login_page)
        login_page.login(user_data['user']['email'], password)
        main_page.make_order()
        button = main_page.find_element(main_page.button_close_popup)
        main_page.script_click(button)
        button = main_page.find_element(main_page.profile_button)
        main_page.script_click(button)
        button = main_page.wait_clickable(profile_page.button_order_history)
        main_page.script_click(button)
        main_page.wait_present(profile_page.first_order_number)
        order_number_history = main_page.find_element(profile_page.first_order_number).text
        button = main_page.find_element(main_page.button_feed)
        main_page.script_click(button)
        main_page.wait_present(feed_page.ul_locator)
        main_page.wait_visible(feed_page.list_items)
        main_page.wait_order_number_in_element(order_number_history, feed_page.list_items)
        orders_in_feed = [item.text for item in feed_page.find_elements(feed_page.text_in_list)]

        assert order_number_history in orders_in_feed

    @allure.title("Тест счетчик всех заказов увеличивается после сделанного заказа")
    def test_all_orders_counter_increase(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        user_data, password = create_user
        main_page.open(Links.link_login_page)
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visible(main_page.div_first_bread_in_bread_section)
        main_page.open(Links.feed_page)
        count_before = main_page.wait_visible(feed_page.count_all_orders).text
        main_page.open(Links.base_url)
        main_page.make_order()
        button = main_page.find_element(main_page.button_close_popup)
        main_page.script_click(button)
        main_page.open(Links.feed_page)
        main_page.wait_count_increase(feed_page.count_all_orders, count_before)
        count_after = feed_page.wait_visible(feed_page.count_all_orders).text

        assert int(count_before) == int(count_after) - 1

    @allure.title("Тест счетчик заказов за сегодня увеличивается после сделанного заказа")
    def test_today_orders_counter_increase(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        user_data, password = create_user
        main_page.open(Links.link_login_page)
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visible(main_page.div_first_bread_in_bread_section)
        main_page.open(Links.feed_page)
        count_before = main_page.wait_visible(feed_page.count_today_orders).text
        main_page.open(Links.base_url)
        main_page.make_order()
        button = main_page.find_element(main_page.button_close_popup)
        main_page.script_click(button)
        main_page.open(Links.feed_page)
        main_page.wait_text_present(feed_page.count_today_orders, f'{int(count_before) + 1}')
        count_after = main_page.wait_visible(feed_page.count_today_orders).text

        assert int(count_before) == int(count_after) - 1

    @allure.title("Тест отображается корректный номер заказа в поле 'В работе'")
    def test_correct_number_shown_in_work(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        user_data, password = create_user
        main_page.open(Links.link_login_page)
        login_page.login(user_data['user']['email'], password)
        main_page.wait_visible(main_page.div_first_bread_in_bread_section)
        main_page.open(Links.base_url)
        main_page.make_order()
        order_number = main_page.find_element(main_page.new_order_number).text
        button = main_page.find_element(main_page.button_close_popup)
        main_page.script_click(button)
        main_page.open(Links.feed_page)
        main_page.wait_text_in_element_(order_number, FeedPage.order_number_in_work)
        order_number_in_work = feed_page.find_element(feed_page.order_number_in_work).text

        assert order_number in order_number_in_work
