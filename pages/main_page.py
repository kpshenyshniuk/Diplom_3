from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
    div_drag_and_drop_constructor = (By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div/span/span[1]')
    button_close_popup = (By.XPATH, '//*[@id="root"]/div/section/div[1]/button')
    button_feed = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[2]/a')
    ingredient_detail_section = (By.XPATH, '//*[@id="root"]/div/section[1]')
    ingredient_detail_header = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div/h2')
    first_indegridient_name = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/p')
    close_details_section_button = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/button')
    counter_of_first_bread = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p')
    overlay_make_order = (By.XPATH, '//*[@id="root"]/div/div')
    ordered_details_screen = (By.XPATH, '//*[@id="root"]/div/section')
    new_order_number = (By.XPATH, '//*[@id="root"]/div/section/div[1]/div/h2')
    new_order_text = (By.XPATH, '//*[@id="root"]/div/section/div[1]/div/div[2]/p[1]')
    indegridient_name_details = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/div/p')
    profile_button = (By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX:nth-child(3)')
    overlay = (By.XPATH, "//*[contains(@class, 'Modal_modal_overlay')]")



