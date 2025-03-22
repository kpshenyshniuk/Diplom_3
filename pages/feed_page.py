import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls import Links


class FeedPage(BasePage):

    header = (By.XPATH, '//h1[contains(@class, "text_type_main-large") and contains(text(), "Лента заказов")]')
    first_order = (By.XPATH, '//li[1]//a[contains(@class, "OrderHistory_link__1iNby")]')
    details_section = (By.XPATH, '(//section[contains(@class, "Modal_modal")])[2]')
    order_number_details_screen = (By.XPATH, '//p[contains(@class, "text text_type_digits-default mb-10 mt-5")]')
    order_number_first = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    count_all_orders = (By.XPATH, '//div[@class="undefined mb-15"]//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    count_today_orders = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    order_number_in_work = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li[contains(@class, "text_type_digits-default")]')
    list_items = (By.XPATH, '//ul/li/a[@class="OrderHistory_link__1iNby"]')
    text_in_list = (By.XPATH, '//div/p[@class="text text_type_digits-default"]')
    ul_locator = (By.XPATH, '//div/ul[contains(@class, "OrderFeed_list")]')

    @allure.step("ожидаем отображения header")
    def wait_visible_header(self):
        self.wait_visible(self.header)

    @allure.step("находим на странице header")
    def find_header_main_page(self):
        return self.find_elements(self.header)

    @allure.step("делаем клик на первый заказ в списке")
    def click_first_order(self):
        locator = self.find_element(self.first_order)
        self.script_click(locator)

    @allure.step("ожидаем появление текста в попапе деталей заказа")
    def wait_text_in_details_section(self):
        self.wait_text_in_element_class(self.text_opened, self.details_section)

    @allure.step("находим номер заказа на странице деталей заказа")
    def get_order_number_details_screen(self):
        self.wait_visible(self.order_number_details_screen)
        return self.find_element(self.order_number_details_screen)

    @allure.step("ожидаем отображения списка заказов в DOM")
    def wait_present_ul_locator(self):
        self.wait_present(self.ul_locator)

    @allure.step("ожидаем видимости заказов")
    def wait_visible_list_items(self):
        self.wait_visible(self.list_items)

    @allure.step("ожидаем видимости конкретного номера заказа в списке заказов")
    def wait_visible_order_number_history_in_text_in_list (self, order_number_history):
        self.wait_order_number_in_element(order_number_history, self.text_in_list)

    @allure.step("возвращаем тест заказа")
    def get_text_in_list(self):
        return self.find_elements(self.text_in_list)

    @allure.step("открываем страницу feed")
    def open_feed_page(self):
        self.open(Links.feed_page)

    @allure.step("Ожидаем пока счетчик заказов за все время увелится на 1")
    def wait_all_count_increase(self, count_before):
        self.wait_count_increase(self.count_all_orders, count_before)

    @allure.step("возвращаем нынешнее кол-во заказов за все время")
    def get_all_order_count(self):
        self.wait_visible(self.count_all_orders)
        return self.find_element(self.count_all_orders).text

    @allure.step("возвращаем нынешнее кол-во заказов за сегодня")
    def get_today_order_count(self):
        self.wait_visible(self.count_today_orders)
        return self.find_element(self.count_today_orders).text

    @allure.step("Ожидаем пока счетчик заказов за сегодня увелится на 1")
    def wait_today_count_increase(self, count_before):
        self.wait_count_increase(self.count_today_orders, count_before)

    @allure.step("ожидаем появление номера заказа в графе 'В работе' ")
    def wait_text_in_order_number_in_work(self, text):
        self.wait_text_in_element_(text, self.order_number_in_work)

    @allure.step("возвращаем номера заказа из графе 'В работе' ")
    def get_order_number_in_work(self):
        return self.find_element(self.order_number_in_work).text
