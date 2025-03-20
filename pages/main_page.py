from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Text
from pages.base_page import BasePage


class MainPage(BasePage):
    button_constructor = (By.XPATH, '//a[@href="/" and contains(., "Конструктор")]')  # Локатор кнопка Конструктор
    title_main_page = (By.XPATH, '//h1[text()="Соберите бургер"]')  # Локатор Собери бургер на главной странице
    button_logo = (By.XPATH, "//div//a[@href='/']")  # Локатор ЛОГО stellar burgers
    make_order_button = (
        By.XPATH, '//button[text()="Оформить заказ"]')  # Локатор кнопки оформить заказ на главное странице
    button_enter_account = (By.XPATH, '//button[contains(text(), "Войти в аккаунт")]')  # Локатор кнопки Войти в аккаунт
    button_section_bread = (By.XPATH, '//span[text()="Булки"]')  # Локатор кнопки раздела Булки
    button_section_sauce = (By.XPATH, '//span[text()="Соусы"]')  # Локатор кнопки раздела Соусы
    button_section_fillings = (By.XPATH, '//span[text()="Начинки"]')  # Локатор кнопки раздела Начинки
    div_with_ingredients_and_scroll = (
        By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")]')
    div_first_bread_in_bread_section = (By.XPATH, '//h2[text()="Булки"]/following-sibling::ul[1]/a[1]')
    div_drag_and_drop_constructor = (By.XPATH, '//ul//li[1]//div//span//span[contains(@class, "constructor-element__text")]')
    button_close_popup = (By.XPATH, '//section//div[1]//button[contains(@class, "Modal_modal__close_modified")]')
    button_feed = (By.XPATH, '//header//nav//ul//li//a[@href="/feed"]')
    ingredient_detail_section = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    ingredient_detail_header = (By.XPATH, '//section[1]//div[1]//div//h2[text()="Детали ингредиента"]')
    first_indegridient_name = (By.XPATH, '//ul[1]//a[1]//p[contains(@class, "BurgerIngredient_ingredient__text")]')
    close_details_section_button = (By.XPATH, '//section[1]//div[1]//button[contains(@class, "Modal_modal__close_modified")]')
    counter_of_first_bread = (By.XPATH, '//ul[1]//a[1]//div//p[contains(@class, "counter_counter__num")]')
    overlay_make_order = (By.XPATH, '(//div[contains(@class, "Modal_modal")])[1]')
    ordered_details_screen = (By.XPATH, '//*[@id="root"]/div/section')
    new_order_number = (By.XPATH, '//div//h2[contains(@class, "Modal_modal__title_shadow")]')
    new_order_text = (By.XPATH, '//div//p[text()="Ваш заказ начали готовить"]')
    indegridient_name_details = (By.XPATH, '//section[1]//div//p[contains(@class, "text text_type_main-medium")]')
    profile_button = (By.XPATH, '//header//nav//a[@href="/account"]')
    overlay = (By.XPATH, "//*[contains(@class, 'Modal_modal_overlay')]")

    def drag_and_drop_js(self, source, target):
        js_code = """
            function simulateDragDrop(sourceNode, destinationNode) {
                var event = document.createEvent('HTMLEvents');
                event.initEvent('dragstart', true, true);
                sourceNode.dispatchEvent(event);

                event = document.createEvent('HTMLEvents');
                event.initEvent('drop', true, true);
                destinationNode.dispatchEvent(event);

                event = document.createEvent('HTMLEvents');
                event.initEvent('dragend', true, true);
                sourceNode.dispatchEvent(event);
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js_code, source, target)

    def make_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//h2[text()="Булки"]/following-sibling::ul[1]//a[1]')))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div/span/span[1]')))
        source = self.driver.find_element(*self.div_first_bread_in_bread_section)
        target = self.driver.find_element(*self.div_drag_and_drop_constructor)
        self.drag_and_drop_js(source, target)

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.div_drag_and_drop_constructor, Text.name_first_indegridient))

        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.make_order_button))
        self.driver.execute_script("arguments[0].click();", button)
        WebDriverWait(self.driver, 10).until(
            lambda d: "opened" not in self.driver.find_element(*self.overlay_make_order).get_attribute("class"))
        WebDriverWait(self.driver, 10).until(
            lambda d: "opened" in self.driver.find_element(*self.ordered_details_screen).get_attribute("class"))
