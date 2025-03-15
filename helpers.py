import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_clickable(driver, locator):
    return WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(locator))


def wait_text_present(driver, locator, text):
    return WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element(locator, text))


def wait_present(driver, locator):
    return WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(locator))


def wait_full_page(driver):
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete")


def wait_visible(driver, locator):
    return WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(locator))


def wait_invisible(driver, locator):
    return WebDriverWait(driver, 10).until(
        expected_conditions.invisibility_of_element_located(locator))


def find_element(driver, locator):
    element = driver.find_element(*locator)
    return element

def drag_and_drop(driver, source, target):
    """
    Кросс-браузерная реализация Drag and Drop, работающая в Firefox и Chrome.
    """
    actions = ActionChains(driver)
    actions.click_and_hold(source).move_to_element(target).release().perform()


def drag_and_drop_js(driver, source, target):
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
    driver.execute_script(js_code, source, target)


def find_elements(driver, locator):
    return driver.find_elements(*locator)

