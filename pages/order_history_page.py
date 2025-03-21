import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Text
from pages.base_page import BasePage
from urls import Links


class OrderHistoryPage(BasePage):

    def is_order_history_page_opened(self):
        return self.get_current_url() == Links.order_history_link


