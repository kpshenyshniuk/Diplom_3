from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from data import CommonData
from conftest import driver
from helpers import wait_clickable, wait_present, wait_visible, find_element, wait_text_present
from locators import LocatorsLoginPage, LocatorsMainPage, LocatorsProfilePage, FeedPage
from links import Links
from data import Text


class TestOrderHistoryPage:

    def test_click_on_order(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(user_data['user']['email'])
        find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(password)
        button = wait_visible(driver, LocatorsLoginPage.login_button_login_page)
        button.click()
        wait_visible(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        wait_visible(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        source = find_element(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        target = find_element(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        wait_text_present(driver, LocatorsMainPage.div_drag_and_drop_constructor, Text.name_first_indegridient)
        button = wait_clickable(driver, LocatorsMainPage.make_order_button)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" not in find_element(driver, LocatorsMainPage.overlay_make_order).get_attribute("class"))
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, LocatorsMainPage.ordered_details_screen).get_attribute("class"))
        button = find_element(driver, LocatorsMainPage.button_close_popup)
        button.click()
        button = find_element(driver, LocatorsMainPage.button_feed)
        button.click()
        wait_present(driver, FeedPage.feed_section)
        button = wait_visible(driver, FeedPage.first_order)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, FeedPage.details_section).get_attribute("class"))
        element = wait_visible(driver, FeedPage.order_number_details_screen)

        assert element.is_displayed()


    def test_orders_from_history_page_shown_on_feed_page(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(user_data['user']['email'])
        find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(password)
        button = wait_visible(driver, LocatorsLoginPage.login_button_login_page)
        button.click()
        wait_visible(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        wait_visible(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        source = find_element(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        target = find_element(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        wait_text_present(driver, LocatorsMainPage.div_drag_and_drop_constructor, Text.name_first_indegridient)
        button = wait_clickable(driver, LocatorsMainPage.make_order_button)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" not in find_element(driver, LocatorsMainPage.overlay_make_order).get_attribute("class"))
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, LocatorsMainPage.ordered_details_screen).get_attribute("class"))
        button = find_element(driver, LocatorsMainPage.button_close_popup)
        button.click()
        button = find_element(driver, LocatorsMainPage.profile_button)
        button.click()
        button = wait_clickable(driver, LocatorsProfilePage.button_order_history)
        button.click()
        order_number_history = find_element(driver, LocatorsProfilePage.first_order_number).text
        button = find_element(driver, LocatorsMainPage.button_feed)
        button.click()
        element = wait_text_present(driver, FeedPage.order_number_first, order_number_history) and find_element(driver, FeedPage.order_number_first)
        order_number_feed = element.text.strip()

        assert order_number_history == order_number_feed


    def test_all_orders_counter_increase(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(user_data['user']['email'])
        find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(password)
        button = wait_visible(driver, LocatorsLoginPage.login_button_login_page)
        button.click()
        wait_visible(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        driver.get(Links.feed_page)
        count_before = wait_visible(driver, FeedPage.count_all_orders).text
        driver.get(Links.base_url)
        wait_visible(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        wait_visible(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        source = find_element(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        target = find_element(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        wait_text_present(driver, LocatorsMainPage.div_drag_and_drop_constructor, Text.name_first_indegridient)
        button = wait_clickable(driver, LocatorsMainPage.make_order_button)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" not in find_element(driver, LocatorsMainPage.overlay_make_order).get_attribute("class"))
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, LocatorsMainPage.ordered_details_screen).get_attribute("class"))
        button = find_element(driver, LocatorsMainPage.button_close_popup)
        button.click()
        driver.get(Links.feed_page)
        count_after = wait_visible(driver, FeedPage.count_all_orders).text

        assert int(count_before) == int(count_after) - 1


    def test_today_orders_counter_increase(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(user_data['user']['email'])
        find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(password)
        button = wait_visible(driver, LocatorsLoginPage.login_button_login_page)
        button.click()
        wait_visible(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        driver.get(Links.feed_page)
        count_before = wait_visible(driver, FeedPage.count_today_orders).text
        driver.get(Links.base_url)
        wait_visible(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        wait_visible(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        source = find_element(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        target = find_element(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        wait_text_present(driver, LocatorsMainPage.div_drag_and_drop_constructor, Text.name_first_indegridient)
        button = wait_clickable(driver, LocatorsMainPage.make_order_button)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" not in find_element(driver, LocatorsMainPage.overlay_make_order).get_attribute("class"))
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, LocatorsMainPage.ordered_details_screen).get_attribute("class"))
        button = find_element(driver, LocatorsMainPage.button_close_popup)
        button.click()
        driver.get(Links.feed_page)
        count_after = wait_visible(driver, FeedPage.count_today_orders).text

        assert int(count_before) == int(count_after) - 1


    def test_correct_number_shown_in_work(self, driver, create_user):
        user_data, password = create_user
        driver.get(Links.link_login_page)
        wait_clickable(driver, LocatorsLoginPage.email_field_login_page)
        find_element(driver, LocatorsLoginPage.email_field_login_page).send_keys(user_data['user']['email'])
        find_element(driver, LocatorsLoginPage.password_field_login_page).send_keys(password)
        button = wait_visible(driver, LocatorsLoginPage.login_button_login_page)
        button.click()
        wait_visible(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        wait_visible(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        source = find_element(driver, LocatorsMainPage.div_first_bread_in_bread_section)
        target = find_element(driver, LocatorsMainPage.div_drag_and_drop_constructor)
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        wait_text_present(driver, LocatorsMainPage.div_drag_and_drop_constructor, Text.name_first_indegridient)
        button = wait_clickable(driver, LocatorsMainPage.make_order_button)
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" not in find_element(driver, LocatorsMainPage.overlay_make_order).get_attribute("class"))
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in find_element(driver, LocatorsMainPage.ordered_details_screen).get_attribute("class"))
        order_number = find_element(driver, LocatorsMainPage.new_order_number).text
        button = find_element(driver, LocatorsMainPage.button_close_popup)
        button.click()
        driver.get(Links.feed_page)
        WebDriverWait(driver, 10).until(
            lambda d: order_number in find_element(driver, FeedPage.order_number_in_work).text.strip())
        order_number_in_work = wait_visible(driver, FeedPage.order_number_in_work).text

        assert order_number in order_number_in_work
