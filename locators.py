
class LocatorsLoginPage:
    email_field_login_page = '//label[text()="Email"]/following-sibling::input'   # Локатор для поля Email на логин странице
    password_field_login_page = '//label[text()="Пароль"]/following-sibling::input' # Локатор для поля pawword на логин странице
    login_button_login_page = '//button[text()="Войти"]' # Локатор кнопки Войти на логин странице

    button_restore_password = '//*[@id="root"]/div/main/div/div/p[2]/a'




class LocatorsResetPasswordPage:
    input_new_password_reset_password_page = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div'
    input_code_reset_password_page = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div'
    locator_overlay_reset_password_page = "//*[@id='root']/div/div"
    new_password_field_reset_password_page = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div'
    show_hide_new_password_icon_reset_password_page = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/div'
    header_restore_password = '//*[@id="root"]/div/main/div/h2'
    input_email_field_restore_password_page = '//*[@id="root"]/div/main/div/form/fieldset/div/div/input'
    button_restore_password_restore_page = '//*[@id="root"]/div/main/div/form/button'
    button_enter_forgot_password_page = '//p//following-sibling::a[@href="/login"]' # локатор кнопки Войти на странице Восстановления пароля


class LocatorsRegistrationPage:
    button_enter_register_page = '//p//following-sibling::a[@href="/login"]'  # локатор кнопки Войти на странице Регистрации
    name_field_registration_page = "//label[text()='Имя']/following-sibling::input"  # Локатор поля Имя на странице регистрации
    email_field_registration_page = "//label[text()='Email']/following-sibling::input"  # Локатор поля Email на странице регистрации
    password_field_registration_page = "//label[text()='Пароль']/following-sibling::input"  # Локатор поля Пароль на странице регистрации
    register_button_registration_page = '//button[text()="Зарегистрироваться"]'  # Кнопка Зарегистрироваться на странице регистрации
    error_text_registration_page = '//p[@class="input__error text_type_main-default"]'  # Локатор текста с ошибкой при вводе не валидного пароля

class LocatorsProfilePage:
    exit_button_profile_page = '//button[text()="Выход"]'  # Локатор кнопки выхода из личного профиля
    email_field_profile_page = '//*[@id="root"]/div/main/div/div/div/ul/li[2]/div/div/input'  # Локатор поля с email на странице profile
    button_profile_page = '//a[@href="/account"]'  # Локатор кнопки перехода в личный кабинет
    button_order_history = '//*[@id="root"]/div/main/div/nav/ul/li[2]/a'


class LocatorsMainPage:
    button_constructor = '//a[@href="/" and contains(., "Конструктор")]'  # Локатор кнопка Конструктор
    title_main_page = '//h1[text()="Соберите бургер"]'  # Локатор Собери бургер на главной странице
    button_logo = "//div//a[@href='/']"  # Локатор ЛОГО stellar burgers
    make_order_button = '//button[text()="Оформить заказ"]'  # Локатор кнопки оформить заказ на главное странице
    button_enter_account = '//button[contains(text(), "Войти в аккаунт")]'  # Локатор кнопки Войти в аккаунт
    button_section_bread = '//span[text()="Булки"]'  # Локатор кнопки раздела Булки
    button_section_sauce = '//span[text()="Соусы"]'  # Локатор кнопки раздела Соусы
    button_section_fillings = '//span[text()="Начинки"]'  # Локатор кнопки раздела Начинки
    div_with_ingredients_and_scroll = "div.BurgerIngredients_ingredients__menuContainer__Xu3Mo"
    div_first_bread_in_bread_section = '//h2[text()="Булки"]/following-sibling::ul[1]/a[1]'
    div_drag_and_drop_constructor = '//*[@id="root"]/div/main/section[2]/ul/li[1]/div/span/span[1]'
    button_close_popup = '//*[@id="root"]/div/section/div[1]/button'
    button_feed = '//*[@id="root"]/div/header/nav/ul/li[2]/a'
    ingredient_detail_section = '//*[@id="root"]/div/section[1]'
    ingredient_detail_header = '//*[@id="root"]/div/section[1]'
    first_indegridient_name = '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/p'
    close_details_section_button = '//*[@id="root"]/div/section[1]/div[1]/button'
    counter_of_first_bread = '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p'
    overlay_make_order = '//*[@id="root"]/div/div'
    ordered_details_screen = '//*[@id="root"]/div/section'
    new_order_number = '//*[@id="root"]/div/section/div[1]/div/h2'
    new_order_text = '//*[@id="root"]/div/section/div[1]/div/div[2]/p[1]'

class FeedPage:
    header = '//*[@id="root"]/div/main/div/h1'