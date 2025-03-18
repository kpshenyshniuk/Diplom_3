from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FeedPage(BasePage):
    # Локаторы
    header = (By.XPATH, '//*[@id="root"]/div/main/div/h1')
    feed_section = (By.XPATH, '//*[@id="root"]/div/main/div')
    first_order = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]')
    details_section = (By.XPATH, '//*[@id="root"]/div/section[2]')
    order_number_details_screen = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div/p[1]')
    order_number_first = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]/a/div[1]/p[1]')
    count_all_orders = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[2]/p[2]')
    count_today_orders = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[3]/p[2]')
    order_number_in_work = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/ul[2]/li')
    list_items = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li')
    text_in_list = (By.XPATH, './a/div[1]/p[1]')

    def login(self, username, password):
        """Логин в систему"""
        self.send_keys(self.email_field_login_page, username)
        self.send_keys(self.password_field_login_page, password)
        self.click(self.login_button_login_page)
