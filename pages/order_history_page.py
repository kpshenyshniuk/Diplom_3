import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):

    first_order_number = (By.XPATH, '//p[@class="text text_type_digits-default"]')

    @allure.step("возвращаем номер первого заказа")
    def get_first_order_number_text(self):
        self.wait_present(self.first_order_number)
        return self.find_element(self.first_order_number).text
