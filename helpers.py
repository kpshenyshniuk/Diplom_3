import time

from selenium.common import TimeoutException
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


