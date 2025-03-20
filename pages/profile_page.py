from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):
    exit_button_profile_page = (By.XPATH, '//button[text()="Выход"]')  # Локатор кнопки выхода из личного профиля
    email_field_profile_page = (By.XPATH,'//*[@id="root"]/div/main/div/div/div/ul/li[2]/div/div/input')  # Локатор поля с email на странице profile
    button_profile_page = (By.XPATH, '//a[@href="/account"]')  # Локатор кнопки перехода в личный кабинет
    button_order_history = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[2]/a')
    first_order_number = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[1]/a/div[1]/p[1]')
