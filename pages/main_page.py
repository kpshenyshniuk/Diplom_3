import allure
from selenium.webdriver.common.by import By
from data import Text
from pages.base_page import BasePage
from urls import Links


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
    div_drag_and_drop_constructor = (By.XPATH, '//div//span//span[contains(@class, "constructor-element__text")]')
    button_close_popup = (By.XPATH, '//div//button[contains(@class, "Modal_modal__close_modified")]')
    button_feed = (By.XPATH, '//a[@href="/feed"]')
    ingredient_detail_section = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    ingredient_detail_header = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    first_indegridient_name = (By.XPATH, '//p[contains(@class, "BurgerIngredient_ingredient__text") and text()="Флюоресцентная булка R2-D3"]')
    close_details_section_button = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox__sCy8X pt-10 pb-15")]/following-sibling::button[contains(@class, "Modal_modal__close_modified")]')
    counter_of_first_bread = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/preceding::p[contains(@class, "counter_counter__num")]')
    overlay_make_order = (By.XPATH, '(//div[contains(@class, "Modal_modal")])[1]')
    ordered_details_screen = (By.XPATH, '//div/section')
    new_order_number = (By.XPATH, '//div//h2[contains(@class, "Modal_modal__title_shadow")]')
    new_order_text = (By.XPATH, '//div//p[text()="Ваш заказ начали готовить"]')
    indegridient_name_details = (By.XPATH, '//p[@class="text text_type_main-medium mb-8" and text()="Флюоресцентная булка R2-D3"]')
    profile_button = (By.XPATH, '//a[@href="/account"]')
    overlay = (By.XPATH, "//*[contains(@class, 'Modal_modal_overlay')]")

    @allure.step("Переносим первый элемент из раздела Булки в конструктор заказа")
    def drag_and_drop_js(self, source = None, target= None):
        self.wait_visible(self.div_first_bread_in_bread_section)
        self.wait_visible(self.div_drag_and_drop_constructor)
        source = self.find_element(*self.div_first_bread_in_bread_section)
        target = self.find_element(*self.div_drag_and_drop_constructor)
        self.execute_script(source, target)
        # js_code = """
        #     function simulateDragDrop(sourceNode, destinationNode) {
        #         var event = document.createEvent('HTMLEvents');
        #         event.initEvent('dragstart', true, true);
        #         sourceNode.dispatchEvent(event);
        #
        #         event = document.createEvent('HTMLEvents');
        #         event.initEvent('drop', true, true);
        #         destinationNode.dispatchEvent(event);
        #
        #         event = document.createEvent('HTMLEvents');
        #         event.initEvent('dragend', true, true);
        #         sourceNode.dispatchEvent(event);
        #     }
        #     simulateDragDrop(arguments[0], arguments[1]);
        # """
        # self.driver.execute_script(js_code, source, target)
        self.wait_text_present(self.div_drag_and_drop_constructor, Text.name_first_indegridient)

    @allure.step("Делаем заказ")
    def make_order(self):
        self.wait_visible(self.div_first_bread_in_bread_section)
        self.wait_visible(self.div_drag_and_drop_constructor)
        source = self.find_element(*self.div_first_bread_in_bread_section)
        target = self.find_element(*self.div_drag_and_drop_constructor)
        self.drag_and_drop_js(source, target)
        self.wait_text_present(self.div_drag_and_drop_constructor, Text.name_first_indegridient)
        button = self.wait_clickable(self.make_order_button)
        self.script_click(button)
        self.wait_text_not_in_element_class(self.text_opened, self.overlay_make_order)
        self.wait_text_in_element_class(self.text_opened, self.ordered_details_screen)
        self.wait_len_element(self.new_order_number)

    @allure.step("Ожидаем видимости кнопки Оформить заказ")
    def wait_visible_make_order_button(self):
        self.wait_visible(self.make_order_button)

    @allure.step("Делаим клик на кнопку Конструктор")
    def click_button_constructor(self):
        element = self.wait_clickable(self.button_constructor)
        self.script_click(element)

    @allure.step("Делаим клик на кнопку Лента заканов")
    def click_button_feed(self):
        self.wait_clickable(self.button_feed)
        element = self.wait_clickable(self.button_feed)
        self.script_click(element)

    @allure.step("Делаим клик на на первый ингредиент в разделе Булки")
    def click_div_first_bread_in_bread_section(self):
        element = self.wait_clickable(self.div_first_bread_in_bread_section)
        self.script_click(element)

    @allure.step("Ожидаем видимости заголовка Соберите бургер")
    def wait_visibility_title(self):
        self.wait_visible(self.title_main_page)

    @allure.step("Находим заголовок Соберите бургер")
    def find_title_main_page(self):
        return self.find_elements(self.title_main_page)

    @allure.step("Находим заголовок Детали ингредиента в всплывающем окне деталях ингредиента")
    def find_ingredient_detail_header(self):
        return self.find_element(self.ingredient_detail_header)

    @allure.step("открываем главную страницу")
    def open_main_page(self):
        self.open(Links.base_url)

    @allure.step("возвращаем текст первого ингредиента")
    def get_first_ingredient_name_text(self):
        return self.find_element(self.first_indegridient_name).text

    @allure.step("возвращаем текст первого ингредиента на всплывающем окне деталей ингредиента")
    def get_ingredient_name_details_text(self):
        return self.find_element(self.indegridient_name_details).text

    @allure.step("ожидаем появление теста opened в элемента Деталей ингредиента")
    def wait_text_in_ingredient_detail_section(self):
        self.wait_text_in_element_class(self.text_opened, self.ingredient_detail_section)

    @allure.step("нажимаем на кнопку закрытия всплывающего окна деталей ингредиента")
    def click_close_details_section_button(self):
        element = self.wait_clickable(self.close_details_section_button)
        self.script_click(element)

    @allure.step("ожидаем пока перестанет быть видимым заголовок деталей ингредиента")
    def wait_invisible_ingredient_detail_header(self):
        self.wait_invisible(self.ingredient_detail_header)

    @allure.step("возвращаем количество добавленных в конструктор элементов")
    def get_counter_of_first_bread_text(self):
        return self.find_element(self.counter_of_first_bread).text

    @allure.step("делаем клик на кнопку Оформить заказ")
    def click_make_order_button(self):
        element = self.wait_clickable(self.make_order_button)
        self.script_click(element)

    @allure.step("возвращаем номер нового заказа")
    def get_new_order_number_text(self):
        self.wait_visible(self.new_order_number)
        return self.find_element(self.new_order_number).text

    @allure.step("Делаем клик на кнопку закрытия окна с новым закказом")
    def click_button_close_popup(self):
        self.wait_clickable(self.button_close_popup)
        element = self.wait_clickable(self.button_close_popup)
        self.script_click(element)

    @allure.step("Делаем клик на кнопку профиля пользователя")
    def click_profile_button(self):
        self.wait_clickable(self.profile_button)
        element = self.wait_clickable(self.profile_button)
        self.script_click(element)

    @allure.step("возвращаем текст из покна с новым заказом")
    def get_text_in_new_order_text(self):
        return self.find_element(self.new_order_text).text
