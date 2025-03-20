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
        main_page.open(Links.feed_page)
        url_before = driver.current_url
        button = main_page.wait_clickable(main_page.button_constructor)
        main_page.script_click(button)
        main_page.wait_visible(main_page.title_main_page)
        url_after = driver.current_url

        assert url_after == Links.base_url
        assert url_before != url_after
        assert main_page.find_element(main_page.title_main_page) is not None

    @allure.title("Тест нажатие на кнопку Лента заказов")
    def test_click_on_feed_button(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.open(Links.base_url)
        url_before = driver.current_url
        button = main_page.wait_clickable(main_page.button_feed)
        button.click()
        main_page.wait_visible(feed_page.header)
        url_after = driver.current_url

        assert url_after == Links.feed_page
        assert url_before != url_after
        assert main_page.find_element(feed_page.header) is not None

    @allure.title("Тест нажатие на ингредиент")
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open(Links.base_url)
        indegridient_name = main_page.find_element(main_page.first_indegridient_name).text
        button = main_page.wait_clickable(main_page.div_first_bread_in_bread_section)
        button.click()
        main_page.wait_text_in_element_class(main_page.text_opened, main_page.ingredient_detail_section)
        element = main_page.find_element(main_page.ingredient_detail_header)
        indegridient_name_on_details = main_page.find_element(main_page.indegridient_name_details).text

        assert element.is_displayed()
        assert indegridient_name == indegridient_name_on_details
    @allure.title("Тест нажатие на крестик закрытия окна с деталями онгредиента")
    def test_click_details_close_icon(self, driver):
        main_page = MainPage(driver)
        main_page.open(Links.base_url)
        button = main_page.wait_clickable(main_page.div_first_bread_in_bread_section)
        button.click()
        main_page.wait_text_in_element_class(main_page.text_opened, main_page.ingredient_detail_section)
        main_page.find_element(main_page.close_details_section_button).click()
        main_page.wait_invisible(main_page.ingredient_detail_header)
        element = main_page.find_element(main_page.ingredient_detail_header)

        assert not element.is_displayed()

    @allure.title("Тест счетчик ингредиентов увеличивается после добавление его в заказ")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open(Links.base_url)
        counter_before = main_page.find_element(main_page.counter_of_first_bread).text
        source = main_page.find_element(main_page.div_first_bread_in_bread_section)
        target = main_page.find_element(main_page.div_drag_and_drop_constructor)
        main_page.drag_and_drop_js(source, target)
        main_page.wait_text_present(main_page.div_drag_and_drop_constructor, Text.name_first_indegridient)
        counter_after = main_page.find_element(main_page.counter_of_first_bread).text

        assert int(counter_after) == int(counter_before) + 2

    @allure.title("Тест пользователь может сделать заказ")
    def test_user_can_make_order(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open(Links.link_login_page)
        user_data, password = create_user
        login_page.login(user_data['user']['email'], password)
        main_page.make_order()
        order_number = main_page.find_element(main_page.new_order_number).text

        assert len(order_number) == 6
        assert main_page.find_element(main_page.new_order_text).text == Text.new_order_text
