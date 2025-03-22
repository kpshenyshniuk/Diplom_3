import allure
from data import Text
from conftest import driver
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from urls import Links


class TestMainPage:
    @allure.title("Тест нажатие на кнопку Конструктор")
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        url_before = feed_page.get_current_url()
        main_page.click_button_constructor()
        main_page.wait_visibility_title()
        url_after = main_page.get_current_url()

        assert url_after == Links.base_url
        assert url_before != url_after
        assert main_page.find_title_main_page()

    @allure.title("Тест нажатие на кнопку Лента заказов")
    def test_click_on_feed_button(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.open_main_page()
        url_before = main_page.get_current_url()
        main_page.click_button_feed()
        feed_page.wait_visible_header()
        url_after = feed_page.get_current_url()

        assert url_after == Links.feed_page
        assert url_before != url_after
        assert feed_page.find_header_main_page()

    @allure.title("Тест нажатие на ингредиент")
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        indegridient_name = main_page.get_first_ingredient_name_text()
        main_page.click_div_first_bread_in_bread_section()
        main_page.wait_text_in_ingredient_detail_section()
        element = main_page.find_ingredient_detail_header()
        indegridient_name_on_details = main_page.get_ingredient_name_details_text()

        assert element.is_displayed()
        assert indegridient_name == indegridient_name_on_details

    @allure.title("Тест нажатие на крестик закрытия окна с деталями онгредиента")
    def test_click_details_close_icon(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_div_first_bread_in_bread_section()
        main_page.wait_text_in_element_class(main_page.text_opened, main_page.ingredient_detail_section)
        main_page.click_close_details_section_button()
        main_page.wait_invisible_ingredient_detail_header()
        element = main_page.find_ingredient_detail_header()

        assert not element.is_displayed()

    @allure.title("Тест счетчик ингредиентов увеличивается после добавление его в заказ")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_before = main_page.get_counter_of_first_bread_text()
        main_page.drag_and_drop_js()
        counter_after = main_page.get_counter_of_first_bread_text()

        assert int(counter_after) == int(counter_before) + 2

    @allure.title("Тест пользователь может сделать заказ")
    def test_user_can_make_order(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        user_data, password = create_user
        login_page.open_login_page()
        login_page.login(user_data['user']['email'], password)
        main_page.drag_and_drop_js()
        main_page.make_order()
        order_number = main_page.get_new_order_number_text()

        assert len(order_number) == 6
        assert main_page.get_text_in_new_order_text() == Text.new_order_text
