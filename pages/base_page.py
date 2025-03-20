from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        """Открывает страницу по URL"""
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete")

    def find_element(self, locator):
        """Ищет элемент на странице"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Ищет список элементов на странице"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        """Кликает по элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    def send_keys(self, locator, text):
        """Вводит текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

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

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))

    def wait_text_present(self, locator, text):
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, text))

    def wait_present(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))

    def wait_full_page(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete")

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator))

