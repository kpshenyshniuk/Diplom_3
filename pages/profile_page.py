import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Links


class ProfilePage(BasePage):
    exit_button_profile_page = (By.XPATH, '//button[text()="Выход"]')  # Локатор кнопки выхода из личного профиля
    email_field_profile_page = (By.XPATH,'//*[@name="name" and @type="text"]')  # Локатор поля с email на странице profile
    button_profile_page = (By.XPATH, '//a[@href="/account"]')  # Локатор кнопки перехода в личный кабинет
    button_order_history = (By.XPATH, '//a[@href="/account/order-history"]')
    first_order_number = (By.XPATH, '//p[@class="text text_type_digits-default"]')

    @allure.step("открываем страницу Профиля пользователя")
    def open_profile_page(self):
        self.open(Links.link_profile_page)

    @allure.step("ожидаем видимости кнопки Выход")
    def wait_visible_exit_button_profile_page(self):
        self.wait_visible(self.exit_button_profile_page)

    @allure.step("возвращаем имя класса поля email")
    def get_class_email_field(self):
        return self.find_element(self.email_field_profile_page).get_attribute('value')

    @allure.step("ожидаем текст Account_link_active в элементе ")
    def wait_text_in_button_order_history(self):
        self.wait_text_in_element_class(self.account_link_active, self.button_order_history)

    @allure.step("делаем клик на кнопку Выход")
    def click_on_exit_button(self):
        element = self.wait_clickable(self.exit_button_profile_page)
        self.script_click(element)

    @allure.step("делаем клик на кнопку История заказов")
    def click_on_button_order_history(self):
        self.wait_clickable(self.button_order_history)
        element = self.wait_clickable(self.button_order_history)
        self.script_click(element)
