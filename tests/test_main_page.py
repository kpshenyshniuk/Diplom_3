from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from data import Text
from conftest import driver
from helpers import wait_clickable, wait_text_present, wait_full_page, wait_visible, wait_invisible, find_element
from locators import LocatorsLoginPage, LocatorsMainPage, FeedPage
from links import Links


class TestMainPage:

    def test_click_on_constructor_button(self, driver):
        driver.get(Links.feed_page)
        wait_full_page(driver)
        url_before = driver.current_url
        button = wait_clickable(driver, LocatorsMainPage.button_constructor)
        button.click()
        wait_visible(driver, LocatorsMainPage.title_main_page)
        url_after = driver.current_url

        assert url_after == Links.base_url
        assert url_before != url_after
        assert find_element(driver, LocatorsMainPage.title_main_page) is not None

    def test_click_on_feed_button(self, driver):
        driver.get(Links.base_url)
        wait_full_page(driver)
        url_before = driver.current_url
        button = wait_clickable(driver, LocatorsMainPage.button_feed)
        button.click()
        wait_visible(driver, FeedPage.header)
        url_after = driver.current_url

        assert url_after == Links.feed_page
        assert url_before != url_after
        assert find_element(driver, FeedPage.header) is not None

    def test_click_on_ingredient(self, driver):
        driver.get(Links.base_url)
        wait_full_page(driver)
        indegridient_name = find_element(driver, LocatorsMainPage.first_indegridient_name).text
        button = wait_clickable(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, LocatorsMainPage.ingredient_detail_section).get_attribute("class"))
        element = find_element(driver, LocatorsMainPage.ingredient_detail_header)
        indegridient_name_on_details = find_element(driver, LocatorsMainPage.indegridient_name_details).text

        assert element.is_displayed()
        assert indegridient_name == indegridient_name_on_details

    def test_click_details_close_icon(self, driver):
        driver.get(Links.base_url)
        wait_full_page(driver)
        button = wait_clickable(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, LocatorsMainPage.ingredient_detail_section).get_attribute("class")
        )
        find_element(driver, LocatorsMainPage.close_details_section_button).click()
        wait_invisible(driver, LocatorsMainPage.ingredient_detail_header)
        element = find_element(driver, LocatorsMainPage.ingredient_detail_header)
        assert not element.is_displayed()

    def test_ingredient_counter_increase(self, driver):
        driver.get(Links.base_url)
        wait_full_page(driver)

        counter_before = find_element(driver, LocatorsMainPage.counter_of_first_bread).text
        source = find_element(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        target = find_element(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        wait_text_present(driver, LocatorsMainPage.div_drag_and_drop_constructor, Text.name_first_indegridient)
        counter_after = find_element(driver, LocatorsMainPage.counter_of_first_bread).text

        assert int(counter_after) == int(counter_before) + 2

    def test_user_can_make_order(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(
            user_data['user']['email'])
        find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(
            password)
        login_button = wait_clickable(driver, LocatorsLoginPage.login_button_login_page)
        login_button.click()
        wait_visible(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        wait_visible(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        source = find_element(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        target = find_element(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        wait_text_present(driver, LocatorsMainPage.div_drag_and_drop_constructor, Text.name_first_indegridient)
        button = wait_clickable(driver, LocatorsMainPage.make_order_button)
        button.click()
        WebDriverWait(driver, 10).until(lambda d: "opened" not in find_element(driver, LocatorsMainPage.overlay_make_order).get_attribute("class"))
        WebDriverWait(driver, 10).until(lambda d: "opened" in find_element(driver, LocatorsMainPage.ordered_details_screen).get_attribute("class"))
        order_number = find_element(driver, LocatorsMainPage.new_order_number).text

        assert order_number.isdigit() and len(order_number) == 6
        assert find_element(driver, LocatorsMainPage.new_order_text).text == Text.new_order_text
