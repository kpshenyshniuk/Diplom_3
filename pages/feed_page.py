from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FeedPage(BasePage):

    header = (By.XPATH, '//h1[contains(@class, "text_type_main-large") and contains(text(), "Лента заказов")]')
    first_order = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]/li[1]')
    details_section = (By.XPATH, '(//section[contains(@class, "Modal_modal")])[2]')
    order_number_details_screen = (By.XPATH, '//section[2]/div[1]/div/p[1]')
    order_number_first = (By.XPATH, '//main//ul//li[1]//a//div[1]//p[@class="text text_type_digits-default"]')
    count_all_orders = (By.XPATH, '//main//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    count_today_orders = (By.XPATH, '//main//div//div//div//div[3]//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    order_number_in_work = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li[contains(@class, "text_type_digits-default")]')
    list_items = (By.XPATH, '//div/main/div/div/ul/li')
    text_in_list = (By.XPATH, '//a/div[1]/p')
    ul_locator = (By.XPATH, '//div/main/div/div/ul[contains(@class, "OrderFeed_list")]')
