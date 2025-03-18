from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Text
from conftest import driver
from helpers import wait_clickable, wait_text_present, wait_full_page, wait_visible, wait_invisible, find_element, \
    drag_and_drop, drag_and_drop_js
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from urls import Links
from pages.base_page import BasePage


class TestBasePage:

    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open(Links.feed_page)
        url_before = driver.current_url
        button = main_page.wait_clickable(main_page.button_constructor)
        driver.execute_script("arguments[0].click();", button)
        main_page.wait_visible(main_page.title_main_page)
        url_after = driver.current_url

        assert url_after == Links.base_url
        assert url_before != url_after
        assert main_page.find_element(main_page.title_main_page) is not None

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

    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open(Links.base_url)
        indegridient_name = main_page.find_element(main_page.first_indegridient_name).text
        button = main_page.wait_clickable(main_page.div_first_bread_in_bread_section)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, main_page.ingredient_detail_section).get_attribute("class"))
        element = main_page.find_element(main_page.ingredient_detail_header)
        indegridient_name_on_details = main_page.find_element(main_page.indegridient_name_details).text

        assert element.is_displayed()
        assert indegridient_name == indegridient_name_on_details

    def test_click_details_close_icon(self, driver):
        main_page = MainPage(driver)
        main_page.open(Links.base_url)
        button = main_page.wait_clickable(main_page.div_first_bread_in_bread_section)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, main_page.ingredient_detail_section).get_attribute("class")
        )
        main_page.find_element(main_page.close_details_section_button).click()
        main_page.wait_invisible(main_page.ingredient_detail_header)
        element = main_page.find_element(main_page.ingredient_detail_header)
        assert not element.is_displayed()

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

    def test_user_can_make_order(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open(Links.link_login_page)
        user_data, password = create_user
        main_page.wait_clickable(login_page.email_field_login_page)
        # wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        main_page.send_keys(login_page.email_field_login_page, user_data['user']['email'])
        # find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(
        #     user_data['user']['email'])
        main_page.send_keys(login_page.password_field_login_page, password)

        # find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(
        #     password)
        login_button = main_page.wait_clickable(login_page.login_button_login_page)
        # login_button = wait_clickable(driver, LocatorsLoginPage.login_button_login_page)
        login_button.click()
        main_page.wait_visible(main_page.div_first_bread_in_bread_section)
        # wait_visible(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        main_page.wait_visible(main_page.div_drag_and_drop_constructor)

        # wait_visible(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        source = main_page.find_element(main_page.div_first_bread_in_bread_section)
        # source = find_element(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        target = main_page.find_element(main_page.div_drag_and_drop_constructor)
        # target = find_element(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        main_page.drag_and_drop_js(source, target)
        # drag_and_drop_js(driver, source, target)
        main_page.wait_text_present(main_page.div_drag_and_drop_constructor, Text.name_first_indegridient)
        # wait_text_present(driver, LocatorsMainPage.div_drag_and_drop_constructor, Text.name_first_indegridient)
        button = main_page.wait_clickable(main_page.make_order_button)
        # button = wait_clickable(driver, LocatorsMainPage.make_order_button)
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 10).until(lambda d: "opened" not in find_element(driver, main_page.overlay_make_order).get_attribute("class"))
        WebDriverWait(driver, 10).until(lambda d: "opened" in find_element(driver, main_page.ordered_details_screen).get_attribute("class"))
        order_number = main_page.find_element(main_page.new_order_number).text
        # order_number = find_element(driver, LocatorsMainPage.new_order_number).text

        assert order_number.isdigit() and len(order_number) == 6
        assert main_page.find_element(main_page.new_order_text).text == Text.new_order_text
