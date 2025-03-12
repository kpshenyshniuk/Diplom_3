import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import CommonData
from conftest import driver
from locators import LocatorsLoginPage, LocatorsMainPage, LocatorsProfilePage, FeedPage
from links import Links


class TestMainPage:

    def test_click_on_constructor_button(self, driver):
        driver.get(Links.feed_page)
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
        url_before = driver.current_url
        button = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsMainPage.button_constructor)))
        button.click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LocatorsMainPage.title_main_page))
        )
        url_after = driver.current_url

        assert url_after == Links.base_url
        assert url_before != url_after
        assert driver.find_element(By.XPATH, LocatorsMainPage.title_main_page)


    def test_click_on_feed_button(self, driver):
        driver.get(Links.base_url)
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
        url_before = driver.current_url
        button = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsMainPage.button_feed)))
        button.click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, FeedPage.header))
        )
        url_after = driver.current_url

        assert url_after == Links.feed_page
        assert url_before != url_after
        assert driver.find_element(By.XPATH, LocatorsMainPage.title_main_page)


    def test_click_on_ingredient(self, driver):
        driver.get(Links.base_url)
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
        indegridient_name = driver.find_element(By.XPATH, LocatorsMainPage.first_indegridient_name).text
        button = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsMainPage.div_first_bread_in_bread_section)))
        button.click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in d.find_element(By.XPATH, LocatorsMainPage.ingredient_detail_section).get_attribute("class"))
        element = driver.find_element(By.XPATH, LocatorsMainPage.ingredient_detail_header)
        indegridient_name_on_details = driver.find_element(By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div/p').text

        assert element.is_displayed()
        assert indegridient_name == indegridient_name_on_details


    def test_click_details_сlose_icon(self, driver):
        driver.get(Links.base_url)
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LocatorsMainPage.div_first_bread_in_bread_section))).click()
        WebDriverWait(driver, 10).until(
            lambda d: "opened" in d.find_element(By.XPATH, LocatorsMainPage.ingredient_detail_section).get_attribute("class"))
        element = driver.find_element(By.XPATH, LocatorsMainPage.ingredient_detail_header)
        driver.find_element(By.XPATH, LocatorsMainPage.close_details_section_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, LocatorsMainPage.ingredient_detail_header)))

        assert not element.is_displayed()

    def test_ingredient_counter_increase(self, driver):
        driver.get(Links.base_url)
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
        counter_before = driver.find_element(By.XPATH, LocatorsMainPage.counter_of_first_bread).text
        source = driver.find_element(By.XPATH, LocatorsMainPage.div_first_bread_in_bread_section)
        target = driver.find_element(By.XPATH, LocatorsMainPage.div_drag_and_drop_constructor)
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, LocatorsMainPage.div_drag_and_drop_constructor), "Флюоресцентная булка R2-D3 (верх)"))
        counter_after = driver.find_element(By.XPATH, LocatorsMainPage.counter_of_first_bread).text

        assert int(counter_after) == int(counter_before) + 2





