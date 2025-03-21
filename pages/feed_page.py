from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FeedPage(BasePage):

    header = (By.XPATH, '//h1[contains(@class, "text_type_main-large") and contains(text(), "Лента заказов")]')
    first_order = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]/li[1]')
    details_section = (By.XPATH, '(//section[contains(@class, "Modal_modal")])[2]')
    order_number_details_screen = (By.XPATH, '//p[contains(@class, "text text_type_digits-default mb-10 mt-5")]')
    order_number_first = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    count_all_orders = (By.XPATH, '//div[@class="undefined mb-15"]//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    count_today_orders = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    order_number_in_work = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li[contains(@class, "text_type_digits-default")]')
    list_items = (By.XPATH, '//ul/li/a[@class="OrderHistory_link__1iNby"]')
    text_in_list = (By.XPATH, '//div/p[@class="text text_type_digits-default"]')
    ul_locator = (By.XPATH, '//div/ul[contains(@class, "OrderFeed_list")]')

    def wait_visible_header(self):
        self.wait_visible(self.header)

    def find_header_main_page(self):
        return self.find_elements(self.header)



