from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):
    exit_button_profile_page = (By.XPATH, '//button[text()="Выход"]')  # Локатор кнопки выхода из личного профиля
    email_field_profile_page = (By.XPATH,'//*[@name="name" and @type="text"]')  # Локатор поля с email на странице profile
    button_profile_page = (By.XPATH, '//a[@href="/account"]')  # Локатор кнопки перехода в личный кабинет
    button_order_history = (By.XPATH, '//a[@href="/account/order-history"]')
    first_order_number = (By.XPATH, '//p[@class="text text_type_digits-default"]')
