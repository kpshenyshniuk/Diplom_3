import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    text_opened = 'opened'
    account_link_active = "Account_link_active"
    modal_opened = "Modal_modal_opened"
    input_status_active = 'active'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем указаннную страницу")
    def open(self, url):
        """Открывает страницу по URL"""
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step("Находим указанный элемент")
    def find_element(self, locator):
        """Ищет элемент на странице"""
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Находим указанные элементы")
    def find_elements(self, locator):
        """Ищет список элементов на странице"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Делаем клик на указанный элемент")
    def click(self, locator):
        """Кликает по элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполняем указанное поле указанным текстом")
    def send_keys(self, locator, text):
        """Вводит текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидаем кликабельности элемента")
    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Ожидаем пока элемент не появится в DOM с конкретным текстом")
    def wait_text_present(self, locator, text):
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, text))

    @allure.step("Ожидаем пока элемент не появится в DOM")
    def wait_present(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))

    @allure.step("Ожидаем полной загрузки страницы")
    def wait_full_page(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step("Ожидаем пока элемент не станет видимым на странице")
    def wait_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    @allure.step("Ожидаем пока элемент станет не видимым на странице")
    def wait_invisible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator))

    @allure.step("Ожидаем пока появиться текст в классе элемента")
    def wait_text_in_element_class(self, text, locator):
        WebDriverWait(self.driver, 10).until(
            lambda d: text in self.driver.find_element(*locator).get_attribute("class"))

    @allure.step("Ожидаем пока мсчезнет текст из класса элемента")
    def wait_text_not_in_element_class(self, text, locator):
        WebDriverWait(self.driver, 10).until(
            lambda d: text not in self.driver.find_element(*locator).get_attribute("class"))

    def wait_len_element(self, locator, length = 6):
        WebDriverWait(self.driver, 20).until(
            lambda d: len(d.find_element(*locator).text) == length)

    @allure.step("Ожидаем пока появиться текст в элементе")
    def wait_text_in_element_(self, text, locator):
        WebDriverWait(self.driver, 10).until(
            lambda d: text in self.driver.find_element(*locator).text.strip())

    @allure.step("Ожидаем пока номер заказа появиться в истории заказов")
    def wait_order_number_in_element(self, order_number, locator):
        WebDriverWait(self.driver, 10).until(lambda driver: any(
            order_number in item.text for item in self.driver.find_elements(*locator)))

    @allure.step("Делаем клик через java")
    def script_click(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)

    @allure.step("возвращает нынешнюю url")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидаем пока счетчик заказов увелится на 1")
    def wait_count_increase(self, locator,  count_before):
        WebDriverWait(self.driver, 10).until(
            lambda d: int(self.driver.find_element(*locator).text) == int(count_before) + 1)


    def execute_script(self, source, target):
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
