
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_clickable(driver, locator):
    return WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(locator))

